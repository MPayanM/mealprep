# ui/ui_menu.py
# Renders the menu builder (left column of Daily Menu tab).

import streamlit as st
from data_loader import list_foods

MEALS = ['breakfast', 'snack_1', 'lunch', 'snack_2', 'diner']
MEAL_LABELS = {
    'breakfast': '🌅 Breakfast',
    'snack_1':   '🍎 Snack 1',
    'lunch':     '🍽️ Lunch',
    'snack_2':   '🥜 Snack 2',
    'diner':     '🌙 Dinner',
}


def render_menu():
    """Renders the meal builder. Modifies st.session_state.menu directly."""

    all_foods = list_foods()

    st.subheader("🍽️ Build Your Menu")
    st.caption("Add foods to each meal. Charts update automatically.")
    st.write("")

    for meal in MEALS:
        with st.expander(MEAL_LABELS[meal], expanded=True):
            items     = st.session_state.menu[meal]
            to_remove = []

            for i, item in enumerate(items):
                r1, r2, r3 = st.columns([3, 1, 0.3])
                with r1:
                    items[i]['food'] = st.selectbox(
                        f"Food##{meal}_{i}",
                        options=all_foods,
                        index=all_foods.index(item['food'])
                              if item['food'] in all_foods else 0,
                        label_visibility='collapsed',
                        key=f"food_{meal}_{i}"
                    )
                with r2:
                    items[i]['grams'] = st.number_input(
                        f"g##{meal}_{i}",
                        min_value=0.0,
                        max_value=2000.0,
                        value=float(item['grams']),
                        step=5.0,
                        label_visibility='visible',
                        key=f"grams_{meal}_{i}"
                    )
                with r3:
                    if st.button("✕", key=f"remove_{meal}_{i}"):
                        to_remove.append(i)

            for i in reversed(to_remove):
                st.session_state.menu[meal].pop(i)
                st.session_state['active_tab'] = 1  # ← mantiene pestaña Daily Menu
                st.rerun()

            if st.button("＋ Add food", key=f"add_{meal}"):
                st.session_state.menu[meal].append({
                    'food':  all_foods[0],
                    'grams': 100.0
                })
                st.session_state['active_tab'] = 1  # ← mantiene pestaña Daily Menu
                st.rerun()