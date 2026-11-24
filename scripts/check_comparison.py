from pprint import pprint

from core.config.settings import IFC_FILE, MODEL_DIR

from core.pipeline import (
    process_ifc,
    process_revit_csv,
)

from core.validation.quantity_comparison import (
    compare_quantities,
    summarize_comparison,
)


def main():

    df_ifc = process_ifc(IFC_FILE)

    df_revit = process_revit_csv(MODEL_DIR)

    comparison = compare_quantities(
        df_ifc,
        df_revit
    )

    summary = summarize_comparison(comparison)

    print("\nQuantity Comparison:")

    print(
        comparison[[
            "category",
            "element_count_ifc",
            "element_count_revit",
            "total_volume_m3_ifc",
            "total_volume_m3_revit",
            "volume_difference_m3",
            "status",
        ]].round(6).to_string(index=False)
    )

    print("\nComparison Summary:")

    pprint(summary)

    print("\nQuantity comparison completed!")


if __name__ == "__main__":
    main()