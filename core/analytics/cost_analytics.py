from pathlib import Path

import numpy as np
import pandas as pd

from core.analytics.material_analytics import (
    prepare_material_data,
)


def load_material_prices(
    file_path: Path
) -> pd.DataFrame:

    prices = pd.read_csv(file_path)

    required_columns = {
        "material",
        "unit",
        "unit_price_sek",
        "source",
    }

    missing = required_columns - set(prices.columns)

    if missing:
        raise ValueError(f"Missing price columns: {missing}")

    prices["material"] = prices["material"].str.strip()

    if prices["material"].isna().any() or prices["material"].eq("").any():
        raise ValueError("Missing material name")

    if prices["material"].duplicated().any():
        raise ValueError("Duplicate material prices")

    prices["unit_price_sek"] = pd.to_numeric(
        prices["unit_price_sek"],
        errors="raise"
    )

    if not np.isfinite(prices["unit_price_sek"]).all():
        raise ValueError("Invalid material prices")

    if (prices["unit_price_sek"] < 0).any():
        raise ValueError("Negative material prices")

    if not prices["unit"].eq("m3").all():
        raise ValueError("Unsupported pricing unit")

    return prices


def calculate_element_costs(
    df: pd.DataFrame,
    prices: pd.DataFrame
) -> pd.DataFrame:

    structural = prepare_material_data(df)

    result = structural.merge(
        prices,
        on="material",
        how="left",
        validate="many_to_one"
    )

    result["missing_price"] = (
        result["unit_price_sek"].isna()
    )

    volumes = result["net_volume_m3"]

    result["invalid_volume"] = (
        ~np.isfinite(volumes) | (volumes <= 0)
    )

    result["estimated_cost_sek"] = (
        volumes * result["unit_price_sek"]
    ).mask(result["invalid_volume"])

    return result


def calculate_cost_kpis(
    df_cost: pd.DataFrame
) -> dict:

    total_elements = len(df_cost)

    priced_elements = int(
        df_cost["estimated_cost_sek"].notna().sum()
    )

    total_cost = df_cost[
        "estimated_cost_sek"
    ].sum(min_count=1)

    return {
        "total_estimated_cost_sek": float(total_cost),
        "structural_elements": total_elements,
        "priced_elements": priced_elements,
        "missing_prices": int(
            df_cost["missing_price"].sum()
        ),
        "unestimated_elements": total_elements - priced_elements,
        "cost_coverage_pct": (
            priced_elements / total_elements * 100
            if total_elements else 0.0
        ),
    }


def calculate_cost_by_category(
    df_cost: pd.DataFrame
) -> pd.DataFrame:

    summary = (
        df_cost
        .groupby("category", as_index=False)
        .agg(
            element_count=("global_id", "size"),
            total_volume_m3=(
                "net_volume_m3",
                lambda values: values.sum(min_count=1)
            ),
            estimated_cost_sek=(
                "estimated_cost_sek",
                lambda values: values.sum(min_count=1)
            ),
            missing_prices=("missing_price", "sum"),
        )
    )

    total_cost = summary[
        "estimated_cost_sek"
    ].sum(min_count=1)

    summary["cost_share_pct"] = (
        summary["estimated_cost_sek"] / total_cost * 100
        if pd.notna(total_cost) and total_cost > 0
        else float("nan")
    )

    return summary.sort_values(
        "estimated_cost_sek",
        ascending=False
    ).reset_index(drop=True)