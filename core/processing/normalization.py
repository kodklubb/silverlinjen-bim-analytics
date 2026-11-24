import ifcopenshell
import pandas as pd

from ifcopenshell.util.unit import calculate_unit_scale


QUANTITY_MAPPING = {
    "Length": ("length_m", "length"),
    "Width": ("width_m", "length"),
    "Height": ("height_m", "length"),
    "Depth": ("depth_m", "length"),
    "Perimeter": ("perimeter_m", "length"),

    "NetVolume": ("net_volume_m3", "volume"),
    "GrossVolume": ("gross_volume_m3", "volume"),

    "NetArea": ("net_area_m2", "area"),
    "NetSideArea": ("net_side_area_m2", "area"),
    "NetSurfaceArea": ("net_surface_area_m2", "area"),
    "CrossSectionArea": ("cross_section_area_m2", "area"),
}


def get_unit_scales(
    model: ifcopenshell.file
) -> dict[str, float]:
    """Get project unit conversion factors to SI units."""

    return {
        "length": calculate_unit_scale(
            model, "LENGTHUNIT"
        ),
        "area": calculate_unit_scale(
            model, "AREAUNIT"
        ),
        "volume": calculate_unit_scale(
            model, "VOLUMEUNIT"
        ),
    }


def normalize_quantities(
    quantities: dict,
    scales: dict[str, float]
) -> dict:
    """Normalize IFC quantities to SI units."""

    normalized = {}

    for source, (target, unit_type) in QUANTITY_MAPPING.items():

        value = quantities.get(source)

        normalized[target] = (
            float(value) * scales[unit_type]
            if value is not None
            else None
        )

    return normalized


def normalize_column_name(name: str) -> str:
    """Convert column names to snake_case."""

    return (
        name.strip()
        .lower()
        .replace(" ", "_")
    )


def normalize_csv_columns(
    df: pd.DataFrame
) -> pd.DataFrame:
    """Standardize Revit CSV column names."""

    result = df.copy()

    result.columns = [
        normalize_column_name(col)
        for col in result.columns
    ]

    return result.rename(columns={
        "family_and_type": "name",
        "structural_material": "material",
    })