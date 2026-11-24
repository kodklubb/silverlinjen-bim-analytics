import numpy as np
import pandas as pd

from core.validation.data_quality import (
    missing_values,
    validate_volumes,
    validate_ifc_dataset,
)


def test_missing_values():

    values = pd.Series([
        None,
        "",
        " ",
        "Concrete"
    ])

    assert missing_values(values).sum() == 3


def test_valid_volumes():

    result = validate_volumes(
        pd.Series([7.488, 24.0, 13.888])
    )

    assert result["missing_volumes"] == 0
    assert result["non_finite_volumes"] == 0
    assert result["non_positive_volumes"] == 0


def test_invalid_volumes():

    result = validate_volumes(
        pd.Series([10, None, -5, 0, np.inf])
    )

    assert result["missing_volumes"] == 1
    assert result["non_finite_volumes"] == 1
    assert result["non_positive_volumes"] == 2


def test_duplicate_global_ids():

    df = pd.DataFrame({
        "global_id": ["ID1", "ID1"],
        "category": ["Columns", "Columns"],
        "material": ["Concrete", "Concrete"],
        "net_volume_m3": [7.488, 7.488],
        "is_structural": [True, True]
    })

    result = validate_ifc_dataset(df)

    assert result["duplicate_global_ids"] == 1