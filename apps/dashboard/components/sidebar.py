
import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.title("SILVERLINJEN")

        st.caption("BIM Analytics Platform")

        st.divider()

        st.markdown("**Project:** Silverlinjen")
        st.markdown("**Model:** Viadukten")
        st.markdown("**Section:** Del 1")
        st.markdown("**Data source:** IFC")

        st.divider()

        st.caption("OpenBIM Infrastructure Analytics")
        st.caption("Version 0.1.0")
