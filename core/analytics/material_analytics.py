import pandas as pd

from core.analytics.quantity_analytics import (
    get_structural_elements,
)


def prepare_material_data(
    df: pd.DataFrame
) -> pd.DataFrame:

    structural = get_structural_elements(df)

    structural["material"] = (
        structural["material"]
        .astype("string")
        .str.strip()
        .replace("", pd.NA)
        .fillna("Unknown")
    )

    return structural


def calculate_material_breakdown(
    df: pd.DataFrame
) -> pd.DataFrame:

    structural = prepare_material_data(df)

    summary = (
        structural
        .groupby("material", as_index=False)
        .agg(
            element_count=("global_id", "size"),
            total_volume_m3=(
                "net_volume_m3",
                lambda values: values.sum(min_count=1)
            ),
            average_volume_m3=("net_volume_m3", "mean"),
            category_count=("category", "nunique"),
        )
    )

    total_volume = summary["total_volume_m3"].sum(
        min_count=1
    )

    summary["volume_share_pct"] = (
        summary["total_volume_m3"] / total_volume * 100
        if pd.notna(total_volume) and total_volume > 0
        else float("nan")
    )

    return summary.sort_values(
        "total_volume_m3",
        ascending=False
    ).reset_index(drop=True)


def calculate_material_by_category(
    df: pd.DataFrame
) -> pd.DataFrame:

    structural = prepare_material_data(df)

    summary = (
        structural
        .groupby(
            ["material", "category"],
            as_index=False
        )
        .agg(
            element_count=("global_id", "size"),
            total_volume_m3=(
                "net_volume_m3",
                lambda values: values.sum(min_count=1)
            ),
        )
    )

    return summary.sort_values(
        "total_volume_m3",
        ascending=False
    ).reset_index(drop=True)