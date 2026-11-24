import numpy as np
import pandas as pd


def missing_values(series: pd.Series) -> pd.Series:
    """Identify missing or empty values."""

    return (
        series.isna()
        | series.astype("string").str.strip().eq("").fillna(False)
    )


def validate_volumes(series: pd.Series) -> dict:
    """Validate engineering volume values."""

    values = pd.to_numeric(series, errors="coerce")

    return {
        "missing_volumes": int(
            values.isna().sum()
        ),
        "non_finite_volumes": int(
            (values.notna() & ~np.isfinite(values)).sum()
        ),
        "non_positive_volumes": int(
            (np.isfinite(values) & (values <= 0)).sum()
        ),
    }


def validate_ifc_dataset(df: pd.DataFrame) -> dict:
    """Validate a normalized IFC dataset."""

    structural = df.loc[df["is_structural"]].copy()

    valid_ids = df.loc[
        ~missing_values(df["global_id"]),
        "global_id"
    ]

    return {
        "total_elements": len(df),

        "structural_elements": len(structural),

        "excluded_elements": len(df) - len(structural),

        "duplicate_global_ids": int(
            valid_ids.duplicated().sum()
        ),

        "missing_global_ids": int(
            missing_values(df["global_id"]).sum()
        ),

        "missing_materials": int(
            missing_values(structural["material"]).sum()
        ),

        "unclassified_elements": int(
            df["category"].eq("Unclassified").sum()
        ),

        **validate_volumes(
            structural["net_volume_m3"]
        ),
    }


def validate_revit_dataset(df: pd.DataFrame) -> dict:
    """Validate a normalized Revit CSV dataset."""

    structural = df.loc[df["is_structural"]].copy()

    counts = pd.to_numeric(
        structural["count"],
        errors="coerce"
    )

    valid_counts = (
        counts.notna()
        & np.isfinite(counts)
        & counts.gt(0)
        & counts.mod(1).eq(0)
    )

    marks = structural.get(
        "mark",
        pd.Series(None, index=structural.index)
    )

    return {
        "total_rows": len(df),

        "total_elements": int(counts.sum())
        if valid_counts.all() else None,

        "invalid_counts": int(
            (~valid_counts).sum()
        ),

        "missing_materials": int(
            missing_values(structural["material"]).sum()
        ),

        "missing_marks": int(
            missing_values(marks).sum()
        ),

        "unclassified_elements": int(
            df["category"].eq("Unclassified").sum()
        ),

        **validate_volumes(
            structural["volume_m3"]
        ),
    }