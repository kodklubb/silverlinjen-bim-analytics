import numpy as np
import pandas as pd

from core.config.settings import VOLUME_TOLERANCE_M3


def summarize_ifc(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate IFC quantities by engineering category."""

    structural = df.loc[df["is_structural"]].copy()

    return (
        structural.groupby("category")
        .agg(
            element_count=("global_id", "size"),
            total_volume_m3=(
                "net_volume_m3",
                lambda values: values.sum(min_count=1)
            ),
            invalid_volumes=(
                "net_volume_m3",
                lambda values: (
                    ~np.isfinite(values) | values.le(0)
                ).sum()
            ),
        )
        .reset_index()
    )


def summarize_revit(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate Revit quantities by engineering category."""

    structural = df.loc[df["is_structural"]].copy()

    return (
        structural.groupby("category")
        .agg(
            element_count=(
                "count",
                lambda values: values.sum(min_count=1)
            ),
            total_volume_m3=(
                "volume_m3",
                lambda values: values.sum(min_count=1)
            ),
            invalid_volumes=(
                "volume_m3",
                lambda values: (
                    ~np.isfinite(values) | values.le(0)
                ).sum()
            ),
            invalid_counts=(
                "count",
                lambda values: (
                    ~np.isfinite(values)
                    | values.le(0)
                    | values.mod(1).ne(0)
                ).sum()
            ),
        )
        .reset_index()
    )


def compare_quantities(
    df_ifc: pd.DataFrame,
    df_revit: pd.DataFrame,
    tolerance: float = VOLUME_TOLERANCE_M3,
) -> pd.DataFrame:
    """Compare IFC and Revit category-level quantities."""

    if not np.isfinite(tolerance) or tolerance < 0:
        raise ValueError("Invalid volume tolerance.")

    ifc_summary = summarize_ifc(df_ifc)
    revit_summary = summarize_revit(df_revit)

    comparison = ifc_summary.merge(
        revit_summary,
        on="category",
        how="outer",
        suffixes=("_ifc", "_revit"),
        validate="one_to_one",
        indicator=True,
    )

    comparison["count_difference"] = (
        comparison["element_count_ifc"]
        - comparison["element_count_revit"]
    )

    comparison["volume_difference_m3"] = (
        comparison["total_volume_m3_ifc"]
        - comparison["total_volume_m3_revit"]
    )

    passed = (
        comparison["_merge"].eq("both")
        & comparison["count_difference"].eq(0)
        & comparison["volume_difference_m3"].abs().le(tolerance)
        & comparison["invalid_volumes_ifc"].eq(0)
        & comparison["invalid_volumes_revit"].eq(0)
        & comparison["invalid_counts"].eq(0)
    )

    comparison["status"] = np.where(
        passed,
        "PASSED",
        "FAILED"
    )

    return comparison


def summarize_comparison(comparison: pd.DataFrame) -> dict:
    """Generate comparison KPIs."""

    total = len(comparison)

    passed = int(
        comparison["status"].eq("PASSED").sum()
    )

    failed = total - passed

    differences = comparison[
        "volume_difference_m3"
    ].abs()

    return {
        "categories_compared": total,

        "passed_categories": passed,

        "failed_categories": failed,

        "total_ifc_volume_m3": float(
            comparison["total_volume_m3_ifc"].sum(min_count=1)
        ),

        "total_revit_volume_m3": float(
            comparison["total_volume_m3_revit"].sum(min_count=1)
        ),

        "total_absolute_difference_m3": (
            float(differences.sum())
            if total and np.isfinite(differences).all()
            else None
        ),

        "agreement_rate_pct": (
            round(passed / total * 100, 2)
            if total else None
        ),
    }