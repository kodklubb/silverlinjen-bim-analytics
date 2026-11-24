
import streamlit as st

from apps.dashboard.components.sidebar import render_sidebar
from apps.dashboard.views.overview import render as render_overview


st.set_page_config(
    page_title="Silverlinjen BIM Analytics",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="expanded",
)


navigation = st.navigation(
    [
        st.Page(
            render_overview,
            title="Overview",
            icon=":material/dashboard:",
            default=True,
        ),
        st.Page(
            "views/quantities.py",
            title="Quantity Take-Off",
            icon=":material/layers:",
        ),
        st.Page(
            "views/materials.py",
            title="Material Analytics",
            icon=":material/category:",
        ),
        st.Page(
            "views/costs.py",
            title="Cost Estimation",
            icon=":material/calculate:",
        ),
        st.Page(
            "views/carbon.py",
            title="Carbon Analysis",
            icon=":material/eco:",
        ),
        st.Page(
            "views/quality.py",
            title="Data Quality",
            icon=":material/verified:",
        ),
        st.Page(
            "views/comparison.py",
            title="IFC vs. Revit",
            icon=":material/compare_arrows:",
        ),
        st.Page(
            "views/model_viewer.py",
            title="3D Model Viewer",
            icon=":material/view_in_ar:",
        ),
        st.Page(
            "views/scenarios.py",
            title="Scenario Analysis",
            icon=":material/tune:",
        ),
        st.Page(
            "views/reports.py",
            title="Reports & Export",
            icon=":material/download:",
        ),
    ]
)

render_sidebar()

navigation.run()
