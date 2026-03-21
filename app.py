# app.py
# Entry point. Orchestrates tabs and session state.
# Run with: streamlit run app.py

import streamlit as st
from ui.ui_profile import render_profile
from ui.ui_menu    import render_menu
from ui.ui_charts  import render_charts

MEALS = ['breakfast', 'snack_1', 'lunch', 'snack_2', 'diner']

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Meal Prep Tracker",
    page_icon="🥗",
    layout="wide"
)

st.markdown("""
    <style>
        /* General text */
        p, div, span, label, input {
            font-size: 14px !important;
        }
        /* Captions */
        .st-emotion-cache-16idsys p {
            font-size: 14px !important;
        }
        /* Selectbox and number input text */
        .stSelectbox div, .stNumberInput div {
            font-size: 14px !important;
        }
        /* Expander labels */
        .streamlit-expanderHeader {
            font-size: 15px !important;
        }
        /* Metric labels */
        [data-testid="stMetricLabel"] {
            font-size: 14px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if 'menu' not in st.session_state:
    st.session_state.menu = {meal: [] for meal in MEALS}

if 'profile' not in st.session_state:
    st.session_state.profile = {
        'weight_kg': 75.0,
        'height_cm': 175.0,
        'age':       25,
        'sex':       'male',
        'activity':  'moderate',
        'objective': 'maintain',
    }

if 'active_tab' not in st.session_state:
    st.session_state['active_tab'] = 0

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🥗 Meal Prep Tracker")
st.caption("Track your daily macros against personalized nutritional goals.")
st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["👤  Profile & Goals", "🍽️  Daily Menu"])

with tab1:
    render_profile()

with tab2:
    left, right = st.columns([1, 1], gap="large")
    with left:
        render_menu()
    with right:
        render_charts()