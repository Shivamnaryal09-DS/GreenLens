"""
streamlit_app.py
────────────────────────────────────────────────────────────────────
GreenLens — Main Entry Point
Run with:  streamlit run streamlit_app.py
────────────────────────────────────────────────────────────────────
"""

import streamlit as st

from config.settings import APP_TITLE, APP_ICON, APP_VERSION, ANALYSIS_DATE, CITY_REGISTRY, DEFAULT_CITY
from utils.styling import inject_css

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

with st.sidebar:
    st.markdown(
        f'<div class="sidebar-brand">{APP_ICON} GreenLens</div>',
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_city_key = st.selectbox(
        "🌆 City",
        options=list(CITY_REGISTRY.keys()),
        index=list(CITY_REGISTRY.keys()).index(DEFAULT_CITY),
    )
    city_cfg = CITY_REGISTRY[selected_city_key]
    st.session_state["city_cfg"] = city_cfg
    st.session_state["city_key"] = selected_city_key

    st.markdown("---")

    page = st.radio(
        "🗂 Pages",
        options=[
            "📊 Dashboard",
            "🗺️ Risk Map",
            "🔬 Policy Simulator",
            "📈 Analytics",
            "⚙️ Settings",
        ],
    )

    st.markdown("---")
    st.markdown(
        f'<div class="sidebar-meta" style="opacity:0.55; font-size:0.67rem;">'
        f"v{APP_VERSION} &nbsp;·&nbsp; {city_cfg['n_wards']} wards &nbsp;·&nbsp; demo"
        f"</div>",
        unsafe_allow_html=True,
    )

# ── Page Router ───────────────────────────────────────────────────
if "Dashboard" in page:
    from pages.dashboard import render
    render()

elif "Map" in page:
    from pages.risk_map import render
    render()

elif "Simulator" in page:
    from pages.simulator import render
    render()

elif "Analytics" in page:
    from pages.analytics import render
    render()

elif "Settings" in page:
    from pages.settings import render
    render()
