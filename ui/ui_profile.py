# ui/ui_profile.py
# Renders the Profile & Goals tab.

import streamlit as st
from goals import calculate_goals


def render_profile(t: dict):
    """Renders the full Profile & Goals tab using translations dict t."""

    st.subheader(t['profile_title'])
    st.caption(t['profile_caption'])
    st.write("")

    c1, c2, c3 = st.columns(3)
    with c1:
        weight = st.number_input(t['weight'], min_value=30.0, max_value=250.0,
                                 value=st.session_state.profile['weight_kg'],
                                 step=0.5)
    with c2:
        height = st.number_input(t['height'], min_value=100.0, max_value=250.0,
                                 value=st.session_state.profile['height_cm'],
                                 step=0.5)
    with c3:
        age = st.number_input(t['age'], min_value=10, max_value=100,
                              value=st.session_state.profile['age'],
                              step=1)

    c4, c5, c6 = st.columns(3)
    with c4:
        sex_options = [t['sex_male'], t['sex_female']]
        sex_keys    = ['male', 'female']
        sex_label   = st.selectbox(
            t['sex'],
            options=sex_options,
            index=sex_keys.index(st.session_state.profile['sex'])
        )
        sex = sex_keys[sex_options.index(sex_label)]

    with c5:
        act_keys   = list(t['activity_options'].keys())
        act_labels = list(t['activity_options'].values())
        act_label  = st.selectbox(
            t['activity'],
            options=act_labels,
            index=act_keys.index(st.session_state.profile['activity'])
        )
        activity = act_keys[act_labels.index(act_label)]

    with c6:
        obj_keys   = list(t['objective_options'].keys())
        obj_labels = list(t['objective_options'].values())
        obj_label  = st.selectbox(
            t['goal'],
            options=obj_labels,
            index=obj_keys.index(st.session_state.profile['objective'])
        )
        objective = obj_keys[obj_labels.index(obj_label)]

    st.write("")
    if st.button(t['save_profile'], type="primary"):
        st.session_state.profile = {
            'weight_kg': weight,
            'height_cm': height,
            'age':       age,
            'sex':       sex,
            'activity':  activity,
            'objective': objective,
        }
        st.success(t['profile_saved'])

    user_goals = calculate_goals(st.session_state.profile)
    g = user_goals

    st.divider()
    st.subheader(t['targets_title'])
    st.caption(t['targets_caption'])
    st.write("")

    gc1, gc2, gc3, gc4 = st.columns(4)
    gc1.metric(f"🔥 {t['calories']}", f"{g['calories_min']}–{g['calories_max']} kcal")
    gc2.metric(f"💪 {t['protein']}",  f"{g['protein_min']}–{g['protein_max']} g")
    gc3.metric(f"🍞 {t['carbs']}",    f"{g['carbs_min']}–{g['carbs_max']} g")
    gc4.metric(f"🥑 {t['fat']}",      f"{g['fat_min']}–{g['fat_max']} g")

    st.write("")
    p = st.session_state.profile
    sex_label      = t['sex_male'] if p['sex'] == 'male' else t['sex_female']
    activity_label = t['activity_options'][p['activity']]
    objective_label = t['objective_options'][p['objective']]

    st.info(
        f"{t['based_on']}: **{p['weight_kg']}kg · "
        f"{p['height_cm']}cm · "
        f"{p['age']}y · "
        f"{sex_label} · "
        f"{activity_label} · "
        f"{objective_label}**"
    )