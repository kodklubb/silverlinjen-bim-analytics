from pprint import pprint

from core.config.settings import IFC_FILE
from core.pipeline import process_ifc

from core.analytics.quantity_analytics import (
    calculate_quantity_kpis,
    calculate_category_breakdown,
)


def main():

    df = process_ifc(IFC_FILE)

    kpis = calculate_quantity_kpis(df)

    breakdown = calculate_category_breakdown(df)

    print("\nQuantity KPIs:")
    pprint(kpis)

    print("\nCategory Breakdown:")
    print(
        breakdown.round(3).to_string(index=False)
    )

    print("\nQuantity analytics completed successfully!")


if __name__ == "__main__":
    main()