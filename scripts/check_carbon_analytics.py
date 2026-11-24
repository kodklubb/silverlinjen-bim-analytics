from pprint import pprint

from core.config.settings import IFC_FILE
from core.pipeline import process_ifc

from core.analytics.carbon_analytics import (
    load_emission_factors,
    calculate_element_emissions,
    calculate_carbon_kpis,
    calculate_carbon_by_category,
)


def main():

    root = IFC_FILE.resolve().parents[3]

    factor_file = (
        root / "data/reference/emission_factors.csv"
    )

    df = process_ifc(IFC_FILE)

    factors = load_emission_factors(factor_file)

    df_carbon = calculate_element_emissions(
        df,
        factors
    )

    kpis = calculate_carbon_kpis(df_carbon)

    category_carbon = calculate_carbon_by_category(
        df_carbon
    )

    print("\nEmission Factors:")
    print(factors.to_string(index=False))

    print("\nCarbon KPIs:")
    pprint(kpis)

    print("\nCarbon by Category:")
    print(
        category_carbon.round(3).to_string(index=False)
    )

    print("\nCarbon analytics completed successfully!")


if __name__ == "__main__":
    main()