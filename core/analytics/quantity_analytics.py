import pandas as pd


def get_structural_elements(
    df: pd.DataFrame
) -> pd.DataFrame:

    return df.loc[df["is_structural"]].copy()


def calculate_quantity_kpis(
    df: pd.DataFrame
) -> dict:

    structural = get_structural_elements(df)

    total_volume = structural[
        "net_volume_m3"
    ].sum(min_count=1)

    return {
        "total_elements": len(df),
        "structural_elements": len(structural),
        "excluded_elements": len(df) - len(structural),
        "total_volume_m3": float(total_volume),
        "category_count": structural["category"].nunique(),
        "material_count": structural["material"].nunique(),
    }


def calculate_category_breakdown(
    df: pd.DataFrame
) -> pd.DataFrame:

    structural = get_structural_elements(df)

    summary = (
        structural
        .groupby("category", as_index=False)
        .agg(
            element_count=("global_id", "count"),
            total_volume_m3=(
                "net_volume_m3",
                lambda values: values.sum(min_count=1)
            ),
            average_volume_m3=("net_volume_m3", "mean"),
            min_volume_m3=("net_volume_m3", "min"),
            max_volume_m3=("net_volume_m3", "max"),
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