import pandas as pd
import pytest

from core.config.settings import IFC_FILE
from core.pipeline import process_ifc

from core.analytics.carbon_analytics import (
    load_emission_factors,
    calculate_element_emissions,
    calculate_carbon_kpis,
    calculate_carbon_by_category,
)


@pytest.fixture(scope="module")
def bim_data():
    return process_ifc(IFC_FILE)


@pytest.fixture(scope="module")
def emission_factors():

    root = IFC_FILE.resolve().parents[3]

    return load_emission_factors(
        root / "data/reference/emission_factors.csv"
    )


@pytest.fixture(scope="module")
def carbon_data(bim_data, emission_factors):

    return calculate_element_emissions(
        bim_data,
        emission_factors
    )


def test_total_structural_elements(bim_data):

    structural = bim_data[bim_data["is_structural"]]

    assert len(structural) == 33


def test_total_concrete_volume(bim_data):

    structural = bim_data[bim_data["is_structural"]]

    assert structural["net_volume_m3"].sum() == (
        pytest.approx(4548.444)
    )


def test_material_coverage(bim_data):

    structural = bim_data[bim_data["is_structural"]]

    assert structural["material"].notna().all()


def test_carbon_total(carbon_data):

    kpis = calculate_carbon_kpis(carbon_data)

    assert kpis["total_co2e_kg"] == (
        pytest.approx(1137111.0)
    )


def test_carbon_tonnes(carbon_data):

    kpis = calculate_carbon_kpis(carbon_data)

    assert kpis["total_co2e_tonnes"] == (
        pytest.approx(1137.111)
    )


def test_carbon_coverage(carbon_data):

    kpis = calculate_carbon_kpis(carbon_data)

    assert kpis["carbon_coverage_pct"] == 100.0


def test_missing_emission_factors(carbon_data):

    kpis = calculate_carbon_kpis(carbon_data)

    assert kpis["missing_emission_factors"] == 0


def test_carbon_category_count(carbon_data):

    summary = calculate_carbon_by_category(
        carbon_data
    )

    assert len(summary) == 5


def test_carbon_share(carbon_data):

    summary = calculate_carbon_by_category(
        carbon_data
    )

    assert summary["carbon_share_pct"].sum() == (
        pytest.approx(100.0)
    )


def test_bridge_deck_emissions(carbon_data):

    summary = calculate_carbon_by_category(
        carbon_data
    )

    deck = summary.loc[
        summary["category"] == "Bridge Deck"
    ].iloc[0]

    assert deck["estimated_co2e_kg"] == (
        pytest.approx(911250.0)
    )


def test_unknown_material(bim_data, emission_factors):

    df = bim_data.copy()

    df.loc[
        df["is_structural"], "material"
    ] = "Unknown material"

    result = calculate_element_emissions(
        df,
        emission_factors
    )

    kpis = calculate_carbon_kpis(result)

    assert kpis["missing_emission_factors"] == 33
    assert kpis["carbon_coverage_pct"] == 0.0
    assert pd.isna(kpis["total_co2e_kg"])


def test_invalid_volume(bim_data, emission_factors):

    df = bim_data.copy()

    idx = df[df["is_structural"]].index[0]

    df.loc[idx, "net_volume_m3"] = -10.0

    result = calculate_element_emissions(
        df,
        emission_factors
    )

    assert result["invalid_volume"].sum() == 1
    assert result["estimated_co2e_kg"].isna().sum() == 1