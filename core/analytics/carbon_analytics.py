from pathlib import Path

import numpy as np
import pandas as pd

from core.analytics.material_analytics import (
    prepare_material_data,
)


def load_emission_factors(
    file_path: Path
) -> pd.DataFrame:

    factors = pd.read_csv(file_path)

    required_columns = {
        "material",
        "unit",
        "emission_factor_kgco2e_m3",
        "lifecycle_stage",
        "source",
    }

    missing = required_columns - set(factors.columns)

    if missing:
        raise ValueError(
            f"Missing emission factor columns: {missing}"
        )

    factors["material"] = factors["material"].str.strip()

    if (
        factors["material"].isna().any()
        or factors["material"].eq("").any()
    ):
        raise ValueError("Missing material name")

    if factors["material"].duplicated().any():
        raise ValueError("Duplicate emission factors")

    factors["emission_factor_kgco2e_m3"] = pd.to_numeric(
        factors["emission_factor_kgco2e_m3"],
        errors="raise"
    )

    if not np.isfinite(
        factors["emission_factor_kgco2e_m3"]
    ).all():
        raise ValueError("Invalid emission factors")

    if (
        factors["emission_factor_kgco2e_m3"] < 0
    ).any():
        raise ValueError("Negative emission factors")

    if not factors["unit"].eq("m3").all():
        raise ValueError("Unsupported emission unit")

    if not factors["lifecycle_stage"].eq("A1-A3").all():
        raise ValueError("Unsupported lifecycle stage")

    return factors


def calculate_element_emissions(
    df: pd.DataFrame,
    factors: pd.DataFrame
) -> pd.DataFrame:

    structural = prepare_material_data(df)

    result = structural.merge(
        factors,
        on="material",
        how="left",
        validate="many_to_one"
    )

    result["missing_emission_factor"] = (
        result["emission_factor_kgco2e_m3"].isna()
    )

    volumes = result["net_volume_m3"]

    result["invalid_volume"] = (
        ~np.isfinite(volumes) | (volumes <= 0)
    )

    result["estimated_co2e_kg"] = (
        volumes * result["emission_factor_kgco2e_m3"]
    ).mask(result["invalid_volume"])

    result["estimated_co2e_tonnes"] = (
        result["estimated_co2e_kg"] / 1000
    )

    return result


def calculate_carbon_kpis(
    df_carbon: pd.DataFrame
) -> dict:

    total_elements = len(df_carbon)

    estimated_elements = int(
        df_carbon["estimated_co2e_kg"].notna().sum()
    )

    total_kg = df_carbon[
        "estimated_co2e_kg"
    ].sum(min_count=1)

    return {
        "total_co2e_kg": float(total_kg),
        "total_co2e_tonnes": float(total_kg / 1000),
        "structural_elements": total_elements,
        "estimated_elements": estimated_elements,
        "missing_emission_factors": int(
            df_carbon["missing_emission_factor"].sum()
        ),
        "unestimated_elements": (
            total_elements - estimated_elements
        ),
        "carbon_coverage_pct": (
            estimated_elements / total_elements * 100
            if total_elements else 0.0
        ),
    }


def calculate_carbon_by_category(
    df_carbon: pd.DataFrame
) -> pd.DataFrame:

    summary = (
        df_carbon
        .groupby("category", as_index=False)
        .agg(
            element_count=("global_id", "size"),
            total_volume_m3=(
                "net_volume_m3",
                lambda values: values.sum(min_count=1)
            ),
            estimated_co2e_kg=(
                "estimated_co2e_kg",
                lambda values: values.sum(min_count=1)
            ),
            missing_emission_factors=(
                "missing_emission_factor", "sum"
            ),
        )
    )

    summary["estimated_co2e_tonnes"] = (
        summary["estimated_co2e_kg"] / 1000
    )

    total_kg = summary[
        "estimated_co2e_kg"
    ].sum(min_count=1)

    summary["carbon_share_pct"] = (
        summary["estimated_co2e_kg"] / total_kg * 100
        if pd.notna(total_kg) and total_kg > 0
        else float("nan")
    )

    return summary.sort_values(
        "estimated_co2e_kg",
        ascending=False
    ).reset_index(drop=True)