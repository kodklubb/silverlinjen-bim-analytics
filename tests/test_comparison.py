import pandas as pd
import pytest

from core.validation.quantity_comparison import (
    compare_quantities,
    summarize_comparison,
)


@pytest.fixture
def sample_ifc():

    return pd.DataFrame({
        "global_id": ["ID1"],
        "category": ["Columns"],
        "net_volume_m3": [7.488],
        "is_structural": [True]
    })


@pytest.fixture
def sample_revit():

    return pd.DataFrame({
        "category": ["Columns"],
        "volume_m3": [7.488],
        "count": [1],
        "is_structural": [True]
    })


def test_matching_quantities(sample_ifc, sample_revit):

    result = compare_quantities(
        sample_ifc,
        sample_revit
    )

    assert result.iloc[0]["status"] == "PASSED"


def test_volume_mismatch(sample_ifc, sample_revit):

    sample_revit["volume_m3"] = 10.0

    result = compare_quantities(
        sample_ifc,
        sample_revit
    )

    assert result.iloc[0]["status"] == "FAILED"


def test_count_mismatch(sample_ifc, sample_revit):

    sample_revit["count"] = 2

    result = compare_quantities(
        sample_ifc,
        sample_revit
    )

    assert result.iloc[0]["status"] == "FAILED"


def test_volume_tolerance(sample_ifc, sample_revit):

    sample_revit["volume_m3"] = 7.4885

    result = compare_quantities(
        sample_ifc,
        sample_revit
    )

    assert result.iloc[0]["status"] == "PASSED"


def test_agreement_rate(sample_ifc, sample_revit):

    comparison = compare_quantities(
        sample_ifc,
        sample_revit
    )

    summary = summarize_comparison(comparison)

    assert summary["agreement_rate_pct"] == 100.0


def test_missing_category(sample_ifc, sample_revit):

    sample_revit["category"] = "Beams"

    result = compare_quantities(
        sample_ifc,
        sample_revit
    )

    assert len(result) == 2
    assert result["status"].eq("FAILED").all()