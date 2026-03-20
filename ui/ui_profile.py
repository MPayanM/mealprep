# ui/ui_profile.py
# Renders the Profile & Goals tab.

import streamlit as st
from goals import calculate_goals

ACTIVITY_OPTIONS = {
    'Sedentary (desk job, no exercise)':          'sedentary',
    'Lightly active (1–3 days/week)':             'light',
    'Moderately active (3–5 days/week)':          'moderate',
    'Very active (6–7 days/week)':                'active',
    'Extremely active (physical job + training)': 'very_active',
}
OBJECTIVE_OPTIONS = {
    'Cut (lose fat · −300 kcal deficit)':     'cut',
    'Maintain (stay at current weight)':      'maintain',
    'Bulk (gain muscle · +300 kcal surplus)': 'bulk',
}


def render_profile():
    """Renders the full Profile & Goals tab. Updates st.session_state.profile on save."""

    st.subheader("Your Profile")
    st.caption("Fill in your data. Your nutritional goals are calculated automatically.")
    st.write("")

    c1, c2, c3 = st.columns(3)
    with c1:
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=250.0,
                                 value=st.session_state.profile['weight_kg'],
                                 step=0.5)
    with c2:
        height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0,
                                 value=st.session_state.profile['height_cm'],
                                 step=0.5)
    with c3:
        age = st.number_input("Age", min_value=10, max_value=100,
                              value=st.session_state.profile['age'],
                              step=1)

    c4, c5, c6 = st.columns(3)
    with c4:
        sex = st.selectbox("Sex", options=['male', 'female'],
                           index=['male', 'female'].index(
                               st.session_state.profile['sex']))
    with c5:
        activity_keys   = list(ACTIVITY_OPTIONS.keys())
        activity_values = list(ACTIVITY_OPTIONS.values())
        activity_label  = st.selectbox(
            "Activity level",
            options=activity_keys,
            index=activity_values.index(st.session_state.profile['activity'])
        )
    with c6:
        objective_keys   = list(OBJECTIVE_OPTIONS.keys())
        objective_values = list(OBJECTIVE_OPTIONS.values())
        objective_label  = st.selectbox(
            "Goal",
            options=objective_keys,
            index=objective_values.index(st.session_state.profile['objective'])
        )

    st.write("")
    if st.button("💾  Save Profile", type="primary"):
        st.session_state.profile = {
            'weight_kg': weight,
            'height_cm': height,
            'age':       age,
            'sex':       sex,
            'activity':  ACTIVITY_OPTIONS[activity_label],
            'objective': OBJECTIVE_OPTIONS[objective_label],
        }
        st.success("Profile saved! Your goals have been updated.")

    # Goals
    user_goals = calculate_goals(st.session_state.profile)
    g = user_goals

    st.divider()
    st.subheader("📌 Your Daily Targets")
    st.caption("Calculated from your profile using the Mifflin-St Jeor equation.")
    st.write("")

    gc1, gc2, gc3, gc4 = st.columns(4)
    gc1.metric("🔥 Calories", f"{g['calories_min']}–{g['calories_max']} kcal")
    gc2.metric("💪 Protein",  f"{g['protein_min']}–{g['protein_max']} g")
    gc3.metric("🍞 Carbs",    f"{g['carbs_min']}–{g['carbs_max']} g")
    gc4.metric("🥑 Fat",      f"{g['fat_min']}–{g['fat_max']} g")

    st.write("")
    st.info(
        f"Based on your profile: **{st.session_state.profile['weight_kg']}kg · "
        f"{st.session_state.profile['height_cm']}cm · "
        f"{st.session_state.profile['age']} years · "
        f"{st.session_state.profile['sex']} · "
        f"{st.session_state.profile['activity']} · "
        f"{st.session_state.profile['objective']}**"
    )