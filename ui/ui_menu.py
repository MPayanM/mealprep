# ui/ui_menu.py
# Renders the menu builder with live USDA food search.

import streamlit as st
from data_loader import search_foods, get_macros_by_id

MEALS = ['breakfast', 'snack_1', 'lunch', 'snack_2', 'diner']
MEAL_LABELS = {
    'breakfast': '🌅 Breakfast',
    'snack_1':   '🍎 Snack 1',
    'lunch':     '🍽️ Lunch',
    'snack_2':   '🥜 Snack 2',
    'diner':     '🌙 Dinner',
}


def render_menu():
    """Renders the meal builder with USDA food search."""

    st.subheader("🍽️ Build Your Menu")
    st.caption("Add foods to each meal. Charts update automatically.")
    st.markdown(
        """
        <div style='font-size:18px; margin: 0 0 16px 0;'>
            👉 Quantities are in grams &nbsp;·&nbsp; 1 x 🥚 ~ 50 g
        </div>
        """,
        unsafe_allow_html=True
    )

    for meal in MEALS:
        with st.expander(MEAL_LABELS[meal], expanded=True):
            items     = st.session_state.menu[meal]
            to_remove = []

            for i, item in enumerate(items):
                r1, r2, r3, r4 = st.columns([3, 1, 0.3, 0.3])
                with r1:
                    st.text(item['food'])
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
                    if st.button("✕", key=f"remove_{meal}_{i}"):
                        to_remove.append(i)

            for i in reversed(to_remove):
                st.session_state.menu[meal].pop(i)
                st.session_state['active_tab'] = 1
                st.rerun()

            # Search box
            st.write("")
            query = st.text_input(
                "Search food",
                placeholder="e.g. chicken breast, oats, egg...",
                label_visibility='collapsed',
                key=f"search_{meal}"
            )

            if query:
                with st.spinner("Searching..."):
                    results = search_foods(query)

                if results:
                    options = {r['name']: r['food_id'] for r in results}
                    selected = st.selectbox(
                        "Select food",
                        options=list(options.keys()),
                        label_visibility='collapsed',
                        key=f"select_{meal}"
                    )
                    grams = st.number_input(
                        "Grams",
                        min_value=1.0,
                        max_value=2000.0,
                        value=100.0,
                        step=5.0,
                        label_visibility='collapsed',
                        key=f"new_grams_{meal}"
                    )

                    if st.button("＋ Add", key=f"add_{meal}"):
                        fdc_id = options[selected]
                        macros = get_macros_by_id(fdc_id)
                        if macros:
                            st.session_state.menu[meal].append({
                                'food':   selected,
                                'grams':  grams,
                                'macros': macros
                            })
                            st.session_state['active_tab'] = 1
                            st.rerun()
                else:
                    st.caption("No results found. Try a different search.")