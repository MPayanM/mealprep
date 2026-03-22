# app.py
# Entry point. Language selection → profile → daily menu.
# Run with: streamlit run app.py

import streamlit as st
from i18n.translations import TRANSLATIONS
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
        div, label, input {
            font-size: 16px !important;
        }
        .st-emotion-cache-16idsys p {
            font-size: 16px !important;
        }
        .stSelectbox div, .stNumberInput div {
            font-size: 16px !important;
        }
        .streamlit-expanderHeader {
            font-size: 18px !important;
        }
        [data-testid="stMetricLabel"] p {
            font-size: 11px !important;
        }
        [data-testid="stMetricValue"] {
            font-size: 28px !important;
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

if 'lang' not in st.session_state:
    st.session_state['lang'] = None  # None = not selected yet

# ── Language modal ────────────────────────────────────────────────────────────
if st.session_state['lang'] is None:
    st.markdown("""
        <div style='text-align:center; padding: 60px 0 20px 0;'>
            <h1>🥗 Meal Prep Tracker</h1>
            <p style='font-size:18px; color:gray;'>Select your language · Choisissez votre langue · Selecciona tu idioma</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])

    with col2:
        if st.button("🇨🇴  Español", use_container_width=True):
            st.session_state['lang'] = 'es'
            st.rerun()
    with col3:
        if st.button("🇫🇷  Français", use_container_width=True):
            st.session_state['lang'] = 'fr'
            st.rerun()
    with col4:
        if st.button("🇬🇧  English", use_container_width=True):
            st.session_state['lang'] = 'en'
            st.rerun()

    st.stop()

# ── Language loaded ───────────────────────────────────────────────────────────
t    = TRANSLATIONS[st.session_state['lang']]
lang = st.session_state['lang']

# ── Header ────────────────────────────────────────────────────────────────────
col_title, col_lang = st.columns([6, 1])

with col_title:
    st.title(t['app_title'])
    st.caption(t['app_caption'])

with col_lang:
    st.write("")
    lang_map = {'es': '🇨🇴 ES', 'fr': '🇫🇷 FR', 'en': '🇬🇧 EN'}
    new_lang = st.selectbox(
        t['change_language'],
        options=['es', 'fr', 'en'],
        format_func=lambda x: lang_map[x],
        index=['es', 'fr', 'en'].index(lang),
        label_visibility='collapsed'
    )
    if new_lang != lang:
        st.session_state['lang'] = new_lang
        st.session_state['menu'] = {meal: [] for meal in MEALS}
        st.rerun()

st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs([t['tab_profile'], t['tab_menu']])

with tab1:
    render_profile(t)

with tab2:
    left, right = st.columns([1, 1], gap="large")
    with left:
        render_menu(t, lang)
    with right:
        render_charts(t, lang)