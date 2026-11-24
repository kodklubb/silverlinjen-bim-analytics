
import streamlit as st

from apps.dashboard.data_service import (
    load_bim_data,
    load_structural_data,
)


def render():
    df_bim = load_bim_data()
    df_structural = load_structural_data()

    st.title("Infrastructure Overview")

    st.caption(
        "Silverlinjen — Viadukten | BIM Data Analytics"
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "IFC Elements",
        len(df_bim),
    )

    col2.metric(
        "Structural Elements",
        len(df_structural),
    )

    col3.metric(
        "Concrete Volume",
        f"{df_structural['net_volume_m3'].sum():,.3f} m³",
    )

    col4.metric(
        "Categories",
        df_structural["category"].nunique(),
    )

    st.divider()

    st.subheader("Structural Elements")

    st.dataframe(
        df_structural[
            [
                "global_id",
                "category",
                "name",
                "material",
                "net_volume_m3",
            ]
        ],
        hide_index=True,
        width="stretch",
    )
