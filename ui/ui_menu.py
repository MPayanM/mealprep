# ui/ui_menu.py
# Renders the menu builder with language support and accent-insensitive search.

import streamlit as st
from data_loader import list_foods, get_macros

MEALS = ['breakfast', 'snack_1', 'lunch', 'snack_2', 'diner']


def render_menu(t: dict, lang: str):
    """Renders the meal builder using translations dict t and language lang."""

    all_foods = list_foods(lang)

    st.subheader(t['menu_title'])
    st.caption(t['menu_caption'])
    st.markdown(
        f"<div style='font-size:18px; margin: 0 0 16px 0;'>{t['menu_tip']}</div>",
        unsafe_allow_html=True
    )

    for meal in MEALS:
        label = t['meal_labels'][meal]
        with st.expander(label, expanded=True):
            items     = st.session_state.menu[meal]
            to_remove = []

            # Existing food rows
            for i, item in enumerate(items):
                r1, r2, r3, r4 = st.columns([3, 1, 0.3, 0.3])
                with r1:
                    st.write(item['food'])
                with r2:
                    items[i]['grams'] = st.number_input(
                        "Grams",
                        min_value=0.0,
                        max_value=2000.0,
                        value=float(item['grams']),
                        step=5.0,
                        label_visibility='collapsed',
                        key=f"grams_{meal}_{i}"
                    )
                with r3:
                    st.markdown("<p style='padding-top:8px;color:gray'>g</p>",
                                unsafe_allow_html=True)
                with r4:
                    if st.button(t['remove_btn'], key=f"remove_{meal}_{i}"):
                        to_remove.append(i)

            for i in reversed(to_remove):
                st.session_state.menu[meal].pop(i)
                st.rerun()

            # ── Food selector ─────────────────────────────────────────────────
            st.write("")

            # Placeholder option — empty by default
            options    = [''] + all_foods
            selected   = st.selectbox(
                t['search_placeholder'],
                options=options,
                index=0,
                label_visibility='collapsed',
                key=f"select_{meal}"
            )

            if selected:
                grams = st.number_input(
                    "Grams",
                    min_value=1.0,
                    max_value=2000.0,
                    value=100.0,
                    step=5.0,
                    label_visibility='collapsed',
                    key=f"new_grams_{meal}"
                )

                if st.button(t['add_btn'], key=f"add_{meal}"):
                    macros = get_macros(selected, lang)
                    if macros:
                        st.session_state.menu[meal].append({
                            'food':   selected,
                            'grams':  grams,
                            'macros': macros
                        })
                        st.rerun()