
import streamlit as st
import pandas as pd

from core.config.settings import IFC_FILE
from core.pipeline import process_ifc


@st.cache_data(show_spinner="Loading IFC model...")
def load_bim_data() -> pd.DataFrame:
    return process_ifc(IFC_FILE)


def load_structural_data() -> pd.DataFrame:
    df_bim = load_bim_data()

    return df_bim[
        df_bim["is_structural"]
    ].copy()
