import pytest
import pandas as pd

from core.processing.normalization import (
    normalize_quantities,
    normalize_csv_columns,
    normalize_column_name,
)


def test_length_conversion():

    result = normalize_quantities(
        {"Length": 5200},
        {"length": 0.001, "area": 1, "volume": 1}
    )

    assert result["length_m"] == pytest.approx(5.2)


def test_volume_conversion():

    result = normalize_quantities(
        {"NetVolume": 24},
        {"length": 0.001, "area": 1, "volume": 1}
    )

    assert result["net_volume_m3"] == pytest.approx(24)


def test_missing_quantity():

    result = normalize_quantities(
        {},
        {"length": 0.001, "area": 1, "volume": 1}
    )

    assert result["net_volume_m3"] is None


def test_column_name_normalization():

    assert normalize_column_name(
        "System Length"
    ) == "system_length"


def test_csv_column_normalization():

    df = pd.DataFrame({
        "Family and Type": ["Concrete Column"],
        "Structural Material": ["Concrete"],
        "Volume_m3": [7.488]
    })

    result = normalize_csv_columns(df)

    assert "name" in result.columns
    assert "material" in result.columns
    assert "volume_m3" in result.columns