from core.config.settings import IFC_FILE
from core.pipeline import process_ifc

from core.analytics.material_analytics import (
    calculate_material_breakdown,
    calculate_material_by_category,
)


def main():

    df = process_ifc(IFC_FILE)

    materials = calculate_material_breakdown(df)

    material_categories = calculate_material_by_category(df)

    print("\nMaterial Breakdown:")
    print(materials.round(3).to_string(index=False))

    print("\nMaterial by Category:")
    print(material_categories.round(3).to_string(index=False))

    print("\nMaterial analytics completed successfully!")


if __name__ == "__main__":
    main()