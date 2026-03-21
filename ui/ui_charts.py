# ui/ui_charts.py
# Renders the live results panel (right column of Daily Menu tab).

import streamlit as st
import plotly.graph_objects as go

from tracker import DayTracker
from goals import calculate_goals

MEALS = ['breakfast', 'snack_1', 'lunch', 'snack_2', 'diner']
COLORS = ['#89b4fa', '#a6e3a1', '#fab387']


def _status_icon(val, min_v, max_v):
    if val == 0:    return "⚪"
    if val < min_v: return "🟠"
    if val > max_v: return "🔴"
    return "🟢"


def _build_totals() -> dict:
    """Calculates nutritional totals from current session menu."""
    tracker = DayTracker()
    for meal in MEALS:
        for item in st.session_state.menu[meal]:
            if item['food'] and item['grams'] > 0:
                tracker.add(meal, item['food'], item['grams'])
    return tracker.get_totals()


def _render_metrics(totals: dict, g: dict):
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(
        f"{_status_icon(totals['calories'], g['calories_min'], g['calories_max'])} Calories",
        f"{totals['calories']:.0f} kcal"
    )
    m2.metric(
        f"{_status_icon(totals['protein'], g['protein_min'], g['protein_max'])} Protein",
        f"{totals['protein']:.1f} g"
    )
    m3.metric(
        f"{_status_icon(totals['carbs'], g['carbs_min'], g['carbs_max'])} Carbs",
        f"{totals['carbs']:.1f} g"
    )
    m4.metric(
        f"{_status_icon(totals['fat'], g['fat_min'], g['fat_max'])} Fat",
        f"{totals['fat']:.1f} g"
    )


def _render_charts(totals: dict, g: dict):
    macros     = ['Protein', 'Carbs', 'Fat']
    actual     = [totals['protein'], totals['carbs'], totals['fat']]
    min_vals   = [g['protein_min'], g['carbs_min'], g['fat_min']]
    max_vals   = [g['protein_max'], g['carbs_max'], g['fat_max']]
    macro_cals = [totals['protein'] * 4, totals['carbs'] * 4, totals['fat'] * 9]

    # ── Figure 1: Bar chart ───────────────────────────────────────────────────
    fig_bar = go.Figure()

    fig_bar.add_trace(
        go.Bar(
            x=macros, y=actual,
            marker_color=COLORS,
            opacity=0.85,
            showlegend=False,
            text=[f"{v:.1f}g" for v in actual],
            textposition='outside',
            textfont=dict(size=16),
            hovertemplate='%{x}: %{y:.1f}g<extra></extra>'
        )
    )

    for i in range(len(macros)):
        fig_bar.add_shape(type='line',
                          x0=i - 0.4, x1=i + 0.4,
                          y0=min_vals[i], y1=min_vals[i],
                          line=dict(color='#a6e3a1', dash='dot', width=2))
        fig_bar.add_shape(type='line',
                          x0=i - 0.4, x1=i + 0.4,
                          y0=max_vals[i], y1=max_vals[i],
                          line=dict(color='#f38ba8', dash='dot', width=2))

    fig_bar.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
                                 line=dict(color='#a6e3a1', dash='dot'),
                                 name='Min'))
    fig_bar.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
                                 line=dict(color='#f38ba8', dash='dot'),
                                 name='Max'))

    fig_bar.update_layout(
        title=dict(text="Macros vs. Goals (g)", font=dict(size=24),
                   x=0.5, xanchor='center'),
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='#cdd6f4',
        font=dict(size=16),
        legend=dict(
            orientation='v',
            x=0.95, xanchor='right',
            y=0.95, yanchor='top',
            font=dict(size=15),
            bgcolor='rgba(30,30,46,0.8)',
            bordercolor='#313244',
            borderwidth=1
        ),
        margin=dict(t=50, b=10, l=10, r=10)
    )
    fig_bar.update_xaxes(showgrid=False, tickfont=dict(size=16))
    fig_bar.update_yaxes(showgrid=True, gridcolor='#313244',
                         range=[0, max(max_vals) * 1.2],
                         tickfont=dict(size=16))

    st.plotly_chart(fig_bar, use_container_width=True)

 
# ── Color legend between charts ───────────────────────────────────────────
    st.markdown(
        """
        <div style='text-align:center; font-size:18px; margin: 10px 0 30px 0;'>
            <span style='color:#89b4fa'>■</span> Protein &nbsp;&nbsp;
            <span style='color:#a6e3a1'>■</span> Carbs &nbsp;&nbsp;
            <span style='color:#fab387'>■</span> Fat
        </div>
        """,
        unsafe_allow_html=True
    )

    # ── Figure 2: Pie chart ───────────────────────────────────────────────────
    fig_pie = go.Figure()

    if sum(macro_cals) > 0:
        fig_pie.add_trace(
            go.Pie(
                labels=macros, values=macro_cals,
                marker_colors=COLORS,
                textinfo='label+percent',
                textfont=dict(size=16),
                hole=0.35,
                showlegend=False,
                hovertemplate='%{label}: %{percent}<extra></extra>'
            )
        )
    else:
        fig_pie.add_trace(
            go.Pie(
                labels=['Add foods to see distribution'],
                values=[1],
                marker_colors=['#313244'],
                textinfo='label',
                textfont=dict(size=16),
                hole=0.35,
                showlegend=False
            )
        )

    fig_pie.update_layout(
        title=dict(text="Macro Distribution (% kcal)", font=dict(size=24),
                   x=0.5, xanchor='center'),
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='#cdd6f4',
        font=dict(size=16),
        margin=dict(t=50, b=10, l=10, r=10)
    )

    st.plotly_chart(fig_pie, use_container_width=True)


def render_charts():
    """Renders the full live results panel: metrics + charts."""
    g      = calculate_goals(st.session_state.profile)
    totals = _build_totals()

    st.subheader("📊 Live Results")
    st.write("")
    _render_metrics(totals, g)
    st.write("")
    st.write("")
    _render_charts(totals, g)