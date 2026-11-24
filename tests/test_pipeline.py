import pytest

from core.config.settings import IFC_FILE, MODEL_DIR

from core.pipeline import (
    process_ifc,
    process_revit_csv,
)

from core.validation.data_quality import (
    validate_ifc_dataset,
    validate_revit_dataset,
)

from core.validation.quantity_comparison import (
    compare_quantities,
    summarize_comparison,
)


@pytest.fixture(scope="module")
def ifc_dataset():

    return process_ifc(IFC_FILE)


@pytest.fixture(scope="module")
def revit_dataset():

    return process_revit_csv(MODEL_DIR)


def test_ifc_element_count(ifc_dataset):

    assert len(ifc_dataset) == 34
    assert ifc_dataset["is_structural"].sum() == 33


def test_ifc_total_volume(ifc_dataset):

    structural = ifc_dataset.loc[
        ifc_dataset["is_structural"]
    ]

    assert structural["net_volume_m3"].sum() == pytest.approx(
        4548.444,
        abs=0.001
    )


def test_revit_element_count(revit_dataset):

    structural = revit_dataset.loc[
        revit_dataset["is_structural"]
    ]

    assert len(structural) == 33
    assert structural["count"].sum() == 33


def test_revit_total_volume(revit_dataset):

    structural = revit_dataset.loc[
        revit_dataset["is_structural"]
    ]

    assert structural["volume_m3"].sum() == pytest.approx(
        4548.444,
        abs=0.001
    )


def test_ifc_data_quality(ifc_dataset):

    quality = validate_ifc_dataset(ifc_dataset)

    assert quality["duplicate_global_ids"] == 0
    assert quality["missing_global_ids"] == 0
    assert quality["missing_materials"] == 0
    assert quality["missing_volumes"] == 0
    assert quality["non_finite_volumes"] == 0
    assert quality["non_positive_volumes"] == 0
    assert quality["unclassified_elements"] == 0


def test_revit_data_quality(revit_dataset):

    quality = validate_revit_dataset(revit_dataset)

    assert quality["invalid_counts"] == 0
    assert quality["missing_volumes"] == 0
    assert quality["missing_materials"] == 0
    assert quality["non_finite_volumes"] == 0
    assert quality["non_positive_volumes"] == 0
    assert quality["unclassified_elements"] == 0
    assert quality["missing_marks"] == 33


def test_full_model_comparison(
    ifc_dataset,
    revit_dataset
):

    comparison = compare_quantities(
        ifc_dataset,
        revit_dataset
    )

    summary = summarize_comparison(comparison)

    assert summary["categories_compared"] == 5
    assert summary["passed_categories"] == 5
    assert summary["failed_categories"] == 0
    assert summary["agreement_rate_pct"] == 100.0