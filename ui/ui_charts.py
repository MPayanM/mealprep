# ui/ui_charts.py
# Renders the live results panel (right column of Daily Menu tab).

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=("Macros vs. Goals (g)", "Macro Distribution (% kcal)"),
        specs=[[{"type": "bar"}], [{"type": "pie"}]],
        vertical_spacing=0.15
    )

    # Bar chart
    fig.add_trace(
        go.Bar(
            x=macros, y=actual,
            marker_color=COLORS,
            opacity=0.85,
            name='Actual',
            text=[f"{v:.1f}g" for v in actual],
            textposition='outside',
            textfont=dict(size=14),
            hovertemplate='%{x}: %{y:.1f}g<extra></extra>'
        ),
        row=1, col=1
    )

    # Min / Max lines
    for i in range(len(macros)):
        fig.add_shape(type='line',
                      x0=i - 0.4, x1=i + 0.4,
                      y0=min_vals[i], y1=min_vals[i],
                      line=dict(color='#a6e3a1', dash='dot', width=2),
                      row=1, col=1)
        fig.add_shape(type='line',
                      x0=i - 0.4, x1=i + 0.4,
                      y0=max_vals[i], y1=max_vals[i],
                      line=dict(color='#f38ba8', dash='dot', width=2),
                      row=1, col=1)

    # Legend traces
    fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
                             line=dict(color='#a6e3a1', dash='dot'),
                             name='Min'), row=1, col=1)
    fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
                             line=dict(color='#f38ba8', dash='dot'),
                             name='Max'), row=1, col=1)

    # Pie chart
    if sum(macro_cals) > 0:
        fig.add_trace(
            go.Pie(
                labels=macros, values=macro_cals,
                marker_colors=COLORS,
                textinfo='label+percent',
                textfont=dict(size=14),
                hole=0.35,
                hovertemplate='%{label}: %{percent}<extra></extra>'
            ),
            row=2, col=1
        )
    else:
        fig.add_trace(
            go.Pie(
                labels=['Add foods to see distribution'],
                values=[1],
                marker_colors=['#313244'],
                textinfo='label',
                textfont=dict(size=14),
                hole=0.35
            ),
            row=2, col=1
        )

    fig.update_layout(
        height=700,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='#cdd6f4',
        font=dict(size=30),
        legend=dict(orientation='h', y=0.52,
                    font=dict(size=13),
                    bgcolor='rgba(0,0,0,0)'),
        margin=dict(t=40, b=20, l=10, r=10)
    )
    fig.update_xaxes(showgrid=False, row=1, col=1,
                     tickfont=dict(size=14))
    fig.update_yaxes(showgrid=True, gridcolor='#313244',
                     range=[0, max(max_vals) * 1.2], row=1, col=1,
                     tickfont=dict(size=13))

    st.plotly_chart(fig, use_container_width=True)


def render_charts():
    """Renders the full live results panel: metrics + charts."""
    g      = calculate_goals(st.session_state.profile)
    totals = _build_totals()

    st.subheader("📊 Live Results")
    st.write("")
    _render_metrics(totals, g)
    st.write("")
    _render_charts(totals, g)