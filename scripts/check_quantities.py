from pprint import pprint

import pandas as pd

from core.config.settings import IFC_FILE

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

from core.processing.normalization import (
    get_unit_scales,
    normalize_quantities,
)


def main():

    model = load_ifc(IFC_FILE)
    scales = get_unit_scales(model)

    print("\nUnit scales:")
    pprint(scales)

    records = []

    for element in get_elements(model):

        category = classify_ifc_element(element)

        if not is_structural(category):
            continue

        raw_quantities = extract_quantities(element)

        quantities = normalize_quantities(
            raw_quantities,
            scales
        )

        records.append({
            "global_id": element.GlobalId,
            "category": category,
            **quantities
        })

    df = pd.DataFrame(records)

    summary = df.groupby("category").agg(
        element_count=("global_id", "size"),
        total_volume_m3=("net_volume_m3", "sum")
    )

    print("\nQuantity summary:")
    print(summary.round(3))

    print("\nStructural elements:", len(df))

    print(
        "Missing volumes:",
        df["net_volume_m3"].isna().sum()
    )

    print(
        "Total volume:",
        round(df["net_volume_m3"].sum(), 3),
        "m³"
    )

    print("\nQuantity processing completed!")


if __name__ == "__main__":
    main()