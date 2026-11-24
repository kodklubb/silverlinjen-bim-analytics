
from functools import lru_cache

import pandas as pd
import numpy as np

from core.config.settings import IFC_FILE
from core.pipeline import process_ifc

from core.analytics.quantity_analytics import (
    get_structural_elements,
    calculate_quantity_kpis,
    calculate_category_breakdown,
)

from apps.api.schemas.quantities import QuantityReport


@lru_cache(maxsize=1)
def load_ifc_data() -> pd.DataFrame:
    return process_ifc(IFC_FILE)


def dataframe_to_records(
    df: pd.DataFrame,
) -> list[dict]:

    clean = df.replace(
        [np.inf, -np.inf],
        np.nan,
    )

    clean = clean.astype(object).where(
        pd.notna(clean),
        None,
    )

    return clean.to_dict(orient="records")


def get_quantity_report() -> QuantityReport:

    df = load_ifc_data()

    kpis = calculate_quantity_kpis(df)

    categories = calculate_category_breakdown(df)

    structural = get_structural_elements(df)

    elements = structural[
        [
            "global_id",
            "ifc_class",
            "name",
            "category",
            "material",
            "net_volume_m3",
        ]
    ]

    clean_kpis = dataframe_to_records(
        pd.DataFrame([kpis])
    )[0]

    return QuantityReport(
        project="Silverlinjen",
        model="Viadukten",
        section="Del 1",
        source="IFC",
        kpis=clean_kpis,
        categories=dataframe_to_records(categories),
        elements=dataframe_to_records(elements),
    )
