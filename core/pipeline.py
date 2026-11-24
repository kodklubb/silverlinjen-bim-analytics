from core.ingestion.csv_loader import load_csv_directory

from core.processing.classification import classify_csv_schedule

from core.processing.normalization import normalize_csv_columns

from pathlib import Path

import pandas as pd

from core.ingestion.ifc_loader import (
    load_ifc,
    get_elements,
)

from core.processing.classification import (
    classify_ifc_element,
    is_structural,
)

from core.processing.quantity_extractor import (
    extract_quantities,
)

from core.processing.material_extractor import (
    extract_material,
)

from core.processing.normalization import (
    get_unit_scales,
    normalize_quantities,
)


def process_ifc(
    file_path: str | Path
) -> pd.DataFrame:
    """Transform an IFC model into a normalized BIM dataset."""

    path = Path(file_path)

    model = load_ifc(path)

    scales = get_unit_scales(model)

    records = []

    for element in get_elements(model):

        category = classify_ifc_element(element)

        raw_quantities = extract_quantities(element)

        quantities = normalize_quantities(
            raw_quantities,
            scales
        )

        material = extract_material(element)

        records.append({
            "global_id": element.GlobalId,
            "ifc_class": element.is_a(),
            "name": element.Name,
            "description": element.Description,
            "object_type": element.ObjectType,
            "predefined_type": getattr(
                element, "PredefinedType", None
            ),
            "tag": getattr(element, "Tag", None),

            "category": category,
            "material": material,

            **quantities,

            "is_structural": is_structural(category),

            "source": "IFC",
            "source_file": path.name,
        })

    if not records:
        raise ValueError("No IFC elements found in model.")

    return pd.DataFrame(records)

def process_revit_csv(
    directory: str | Path
) -> pd.DataFrame:
    """Transform Revit CSV schedules into a normalized dataset."""

    datasets = load_csv_directory(directory)

    frames = []

    required_columns = {
        "name",
        "material",
        "volume_m3",
        "count",
    }

    for schedule_name, df in datasets.items():

        normalized = normalize_csv_columns(df)

        missing = required_columns - set(normalized.columns)

        if missing:
            raise ValueError(
                f"Missing columns in {schedule_name}: {missing}"
            )

        category = classify_csv_schedule(schedule_name)

        normalized["category"] = category

        normalized["is_structural"] = is_structural(category)

        normalized["source"] = "Revit CSV"

        normalized["source_file"] = f"{schedule_name}.csv"

        normalized["volume_m3"] = pd.to_numeric(
            normalized["volume_m3"],
            errors="coerce"
        )

        normalized["count"] = pd.to_numeric(
            normalized["count"],
            errors="coerce"
        )

        frames.append(normalized)

    return pd.concat(
        frames,
        ignore_index=True,
        sort=False
    )