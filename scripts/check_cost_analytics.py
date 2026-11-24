from pprint import pprint

from core.config.settings import IFC_FILE
from core.pipeline import process_ifc

from core.analytics.cost_analytics import (
    load_material_prices,
    calculate_element_costs,
    calculate_cost_kpis,
    calculate_cost_by_category,
)


def main():

    root = IFC_FILE.resolve().parents[3]

    price_file = (
        root / "data/reference/material_prices.csv"
    )

    df = process_ifc(IFC_FILE)

    prices = load_material_prices(price_file)

    df_cost = calculate_element_costs(df, prices)

    kpis = calculate_cost_kpis(df_cost)

    category_costs = calculate_cost_by_category(df_cost)

    print("\nMaterial Prices:")
    print(prices.to_string(index=False))

    print("\nCost KPIs:")
    pprint(kpis)

    print("\nCost by Category:")
    print(category_costs.round(3).to_string(index=False))

    print("\nCost analytics completed successfully!")


if __name__ == "__main__":
    main()