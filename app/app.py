from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from components import (
    alert_card,
    analyzer_preview,
    architecture_flow,
    decision_panel,
    floating_decision_cards,
    game_info_panel,
    hero_section,
    page_glass_header,
)
from data_loader import (
    get_alert_window,
    get_daily_for_game,
    get_game_names,
    get_game_score,
    load_alerts,
    load_benchmarks,
    load_game_scores,
)
from gemini_service import GEMINI_MODEL, connection_label, guard_sql, nl_to_sql, run_sql
from styles import inject_global_styles


st.set_page_config(
    page_title="BuyOrWait",
    page_icon=":video_game:",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_global_styles()


def go_to(route: str) -> None:
    if route == "home":
        st.query_params.clear()
    else:
        st.query_params["page"] = route
    st.rerun()


def current_route() -> str:
    route = st.query_params.get("page", "home")
    if isinstance(route, list):
        route = route[0] if route else "home"
    return route if route in PAGES else "home"


def inject_home_shell_styles() -> None:
    st.markdown(
        """
        <style>
        html,
        body,
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"] {
            height: 100vh !important;
            max-height: 100vh !important;
            overflow: hidden !important;
        }
        [data-testid="stSidebar"],
        [data-testid="collapsedControl"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="stActionButton"] {
            display: none !important;
        }
        header[data-testid="stHeader"] {
            display: none !important;
            background: transparent;
            height: 0 !important;
            pointer-events: none;
        }
        .block-container {
            max-width: 100%;
            width: 100vw;
            height: 100vh;
            padding: 0 !important;
            overflow: hidden !important;
        }
        .main .block-container > div {
            padding: 0;
        }
        [data-testid="stElementContainer"],
        div[data-testid="stVerticalBlock"],
        div[data-testid="stVerticalBlock"] > div {
            max-height: 100vh !important;
        }
        [data-testid="stElementContainer"]:has(iframe) {
            position: fixed !important;
            inset: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            z-index: 0;
            overflow: hidden !important;
        }
        iframe,
        iframe[title="st.iframe"],
        iframe[title="streamlit-component"] {
            position: fixed !important;
            inset: 0 !important;
            display: block;
            width: 100vw !important;
            height: 100vh !important;
            max-height: 100vh !important;
            border: 0;
        }
        .st-key-home_action_dock {
            position: fixed !important;
            z-index: 40;
            left: clamp(24px, 5vw, 72px);
            bottom: clamp(32px, 7vh, 78px);
            width: auto !important;
            max-width: min(760px, calc(100vw - 48px));
            pointer-events: auto;
        }
        .st-key-home_action_dock [data-testid="stHorizontalBlock"] {
            gap: 12px;
            flex-wrap: wrap;
        }
        .st-key-home_action_dock .stButton {
            width: auto !important;
        }
        .st-key-home_action_dock .stButton > button {
            min-height: 50px;
            padding: 0 20px;
            border-radius: 18px;
            border-color: oklch(0.95 0.03 220 / 0.42);
            color: oklch(0.98 0.003 84);
            background:
                linear-gradient(145deg, oklch(1 0 0 / 0.34), transparent 34%),
                linear-gradient(180deg, oklch(0.62 0.052 238 / 0.42), oklch(0.29 0.025 248 / 0.52));
            backdrop-filter: blur(24px) saturate(1.55);
            box-shadow:
                inset 0 1px 0 oklch(1 0 0 / 0.34),
                inset 0 -1px 0 oklch(0 0 0 / 0.22),
                0 14px 28px oklch(0 0 0 / 0.18);
            font-weight: 850;
        }
        .st-key-home_action_dock .stButton:first-of-type > button {
            border-color: oklch(0.82 0.15 76 / 0.62);
            background:
                linear-gradient(135deg, oklch(1 0 0 / 0.32), transparent 38%),
                linear-gradient(180deg, oklch(0.75 0.14 73 / 0.62), oklch(0.38 0.06 70 / 0.62));
        }
        .st-key-home_action_dock .stButton > button:hover {
            transform: translateY(-3px);
            border-color: oklch(0.88 0.09 203 / 0.62);
            box-shadow:
                inset 0 1px 0 oklch(1 0 0 / 0.32),
                0 18px 30px oklch(0 0 0 / 0.18),
                0 0 22px oklch(0.83 0.13 203 / 0.16);
        }
        .st-key-home_action_dock .stButton > button:active {
            transform: translateY(1px) scale(0.965);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_navigation(active: str) -> None:
    with st.container(key="page_nav", horizontal=True, gap="small"):
        if st.button("Home", use_container_width=False, type="primary" if active == "home" else "secondary"):
            go_to("home")
        if st.button("Decision Demo", use_container_width=False, type="primary" if active == "dashboard" else "secondary"):
            go_to("dashboard")
        if st.button("Ask AI", use_container_width=False, type="primary" if active == "ask" else "secondary"):
            go_to("ask")
        if st.button("Review Alerts", use_container_width=False, type="primary" if active == "alerts" else "secondary"):
            go_to("alerts")
        if st.button("Why GPU", use_container_width=False, type="primary" if active == "gpu" else "secondary"):
            go_to("gpu")


def home_navigation() -> None:
    with st.container(key="home_action_dock", horizontal=True, gap="small"):
        if st.button("Analyze Product", key="home_nav_dashboard", use_container_width=False, type="primary"):
            go_to("dashboard")
        if st.button("Ask AI", key="home_nav_ask", use_container_width=False):
            go_to("ask")
        if st.button("Review Alerts", key="home_nav_alerts", use_container_width=False):
            go_to("alerts")
        if st.button("Why GPU", key="home_nav_gpu", use_container_width=False):
            go_to("gpu")


def build_sentiment_chart(daily: pd.DataFrame, title: str) -> go.Figure:
    fig = go.Figure()
    fig.add_bar(
        x=daily["date"],
        y=daily["review_volume"],
        name="Review volume",
        yaxis="y2",
        marker_color="rgba(73, 202, 232, 0.32)",
        hovertemplate="%{x|%b %d}<br>Reviews: %{y}<extra></extra>",
    )
    fig.add_trace(
        go.Scatter(
            x=daily["date"],
            y=daily["positive_rate"],
            mode="lines+markers",
            name="Positive rate",
            line=dict(color="#f4b84f", width=3),
            marker=dict(size=6, color="#f4b84f"),
            hovertemplate="%{x|%b %d}<br>Positive: %{y:.1%}<extra></extra>",
        )
    )
    fig.update_layout(
        title=title,
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f2f0ea"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=12, r=12, t=56, b=24),
        yaxis=dict(title="Positive rate", tickformat=".0%", range=[0, 1]),
        yaxis2=dict(title="Review volume", overlaying="y", side="right", showgrid=False),
        hovermode="x unified",
    )
    return fig


def build_alert_chart(window: pd.DataFrame, alert_date: pd.Timestamp) -> go.Figure:
    fig = go.Figure()
    fig.add_bar(
        x=window["date"],
        y=window["review_volume"],
        name="Review volume",
        yaxis="y2",
        marker_color="rgba(244, 184, 79, 0.32)",
    )
    fig.add_trace(
        go.Scatter(
            x=window["date"],
            y=window["negative_rate"],
            mode="lines+markers",
            name="Negative rate",
            line=dict(color="#ff5c59", width=3),
            marker=dict(size=6, color="#ff5c59"),
        )
    )
    fig.add_vline(
        x=alert_date,
        line_color="#ff5c59",
        line_width=2,
        line_dash="dash",
        annotation_text="alert date",
        annotation_position="top right",
    )
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f2f0ea"),
        margin=dict(l=12, r=12, t=26, b=24),
        yaxis=dict(title="Negative rate", tickformat=".0%", range=[0, 1]),
        yaxis2=dict(title="Review volume", overlaying="y", side="right", showgrid=False),
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


def build_benchmark_chart(benchmarks: pd.DataFrame) -> go.Figure:
    rows = benchmarks.loc[benchmarks["stage"] != "End-to-end"]
    fig = go.Figure()
    fig.add_bar(
        y=rows["stage"],
        x=rows["pandas_cpu_time"],
        orientation="h",
        name="pandas CPU",
        marker_color="#ff7a59",
    )
    fig.add_bar(
        y=rows["stage"],
        x=rows["cudf_gpu_time"],
        orientation="h",
        name="cudf.pandas GPU",
        marker_color="#55d98b",
    )
    fig.update_layout(
        template="plotly_dark",
        barmode="group",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f2f0ea"),
        xaxis_title="Runtime (seconds)",
        yaxis_title="",
        margin=dict(l=10, r=10, t=12, b=36),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    fig.update_yaxes(autorange="reversed")
    return fig


def explain_recommendation(game: pd.Series) -> str:
    status = "BUY" if game.buy_confidence_score >= 75 else "WAIT" if game.buy_confidence_score >= 50 else "SKIP"
    if status == "BUY":
        return "Recent weighted sentiment is strong and stable, with no anomaly signal detected."
    if status == "WAIT":
        return "The game shows mixed recent sentiment, so waiting for the next patch or discount is safer."
    return "Recent negative reviews increased sharply, suggesting potential risk."


def page_home() -> None:
    hero_section()
    home_navigation()


def page_dashboard() -> None:
    page_glass_header(
        "Decision Demo",
        "Choose a Steam game and let the AI timing layer turn review momentum into a buy-or-wait recommendation.",
        "dashboard",
    )
    page_navigation("dashboard")
    st.markdown('<div class="section-label">Try the decision engine</div>', unsafe_allow_html=True)
    selected_game = st.selectbox("Paste a Steam game URL or choose a demo game", get_game_names(), index=0)
    game = get_game_score(selected_game)
    daily = get_daily_for_game(selected_game)

    analyzer_preview(game)
    floating_decision_cards(game)

    st.markdown('<div class="dashboard-divider"></div>', unsafe_allow_html=True)
    st.subheader("Dashboard Section")
    left, right = st.columns([0.62, 0.38], gap="large")
    with left:
        game_info_panel(game)
        st.write("")
        st.plotly_chart(
            build_sentiment_chart(daily, f"{selected_game} recent sentiment trend"),
            width="stretch",
        )
    with right:
        decision_panel(float(game.buy_confidence_score))
        st.write("")
        metric_cols = st.columns(2)
        metric_cols[0].metric("Recent positive rate", f"{game.recent_positive_rate:.1%}")
        metric_cols[1].metric("Reviews last 30 days", f"{int(game.review_volume_30d):,}")
        metric_cols[0].metric("Negative rate change", f"{game.negative_rate_change:+.1%}")
        metric_cols[1].metric("Weighted confidence", f"{game.weighted_confidence_score:.0f}/100")

    st.markdown("### Recommendation explanation")
    st.markdown(
        f"""
        <div class="bow-panel">
          <div class="bow-card-value">{explain_recommendation(game)}</div>
          <div class="bow-card-note">
            Signal combines recent positive rate, review-volume stability, weighted confidence, and rolling-window anomaly checks.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_alerts() -> None:
    page_glass_header(
        "Review Bombing Alerts",
        "Track sudden negative-review spikes before they distort a game's buying signal.",
        "alerts",
    )
    page_navigation("alerts")
    alerts = load_alerts()
    scores = load_game_scores()
    latest = alerts["alert_date"].max().strftime("%b %d, %Y")

    cols = st.columns(4)
    with cols[0]:
        alert_card("Total alerts", str(len(alerts)), "rolling-window events", "medium")
    with cols[1]:
        alert_card("Critical alerts", str((alerts.severity == "Critical").sum()), "needs immediate review", "critical")
    with cols[2]:
        alert_card("Games affected", str(alerts.game_name.nunique()), "unique titles", "high")
    with cols[3]:
        alert_card("Latest alert date", latest, "latest event in current source", "medium")

    st.subheader("Filter area")
    f1, f2, f3 = st.columns([0.38, 0.24, 0.38])
    game_filter = f1.multiselect("Game name", sorted(alerts.game_name.unique()), default=sorted(alerts.game_name.unique()))
    severity_filter = f2.multiselect("Severity", ["Critical", "High", "Medium"], default=["Critical", "High", "Medium"])
    date_range = f3.date_input(
        "Date range",
        value=(alerts.alert_date.min().date(), alerts.alert_date.max().date()),
        min_value=alerts.alert_date.min().date(),
        max_value=alerts.alert_date.max().date(),
    )

    filtered = alerts.loc[
        alerts["game_name"].isin(game_filter) & alerts["severity"].isin(severity_filter)
    ].copy()
    if len(date_range) == 2:
        start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        filtered = filtered.loc[(filtered.alert_date >= start) & (filtered.alert_date <= end)]

    st.dataframe(
        filtered[
            [
                "game_name",
                "appid",
                "alert_date",
                "negative_rate",
                "rolling_30d_negative_rate",
                "z_score",
                "review_volume",
                "volume_multiplier",
                "severity",
                "possible_reason",
            ]
        ],
        width="stretch",
        hide_index=True,
    )

    if filtered.empty:
        st.info("No alerts match the current filters.")
        return

    st.subheader("Alert detail view")
    labels = filtered.apply(
        lambda row: f"{row.game_name} | {row.alert_date.strftime('%b %d')} | {row.severity}",
        axis=1,
    ).tolist()
    selected_label = st.selectbox("Select alert", labels)
    selected = filtered.iloc[labels.index(selected_label)]
    window = get_alert_window(selected.game_name, selected.alert_date)
    st.plotly_chart(build_alert_chart(window, selected.alert_date), width="stretch")
    matching_scores = scores.loc[scores.game_name == selected.game_name, "buy_confidence_score"]
    historical_score = f"{matching_scores.iloc[0]:.0f}/100" if not matching_scores.empty else "not available"
    st.markdown(
        f"""
        <div class="bow-panel">
          <div class="bow-card-value">Potential review bombing event for {selected.game_name}</div>
          <div class="bow-card-note">
            Negative rate jumped above the 30-day baseline while review volume also spiked,
            indicating a potential review bombing event. Historical app score:
            {historical_score}.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_ask() -> None:
    page_glass_header(
        "Ask BuyOrWait AI",
        "Turn a plain-English Steam question into a guarded BigQuery query over the aggregated review intelligence tables.",
        "ask",
    )
    page_navigation("ask")

    st.markdown('<div class="section-label">Natural-language review intelligence</div>', unsafe_allow_html=True)
    examples = [
        "Top 10 games by purchase confidence with at least 100k reviews",
        "Which 5 games had the most review-bombing days?",
        "How much faster is the GPU for each pipeline stage?",
    ]
    columns = st.columns(3)
    for index, (column, example) in enumerate(zip(columns, examples)):
        if column.button(example, key=f"ask_example_{index}", use_container_width=True):
            st.session_state["ask_question"] = example

    question = st.text_input(
        "Ask about games, sentiment, alerts, or GPU performance",
        key="ask_question",
        placeholder="Which games recovered after a rough launch?",
    )
    st.caption(
        f"Gemini {GEMINI_MODEL} writes read-only SQL for {connection_label()}; queries are capped at 1 GB scanned."
    )

    if not question:
        st.markdown(
            """
            <div class="bow-panel">
              <div class="bow-card-title">Guarded AI workflow</div>
              <div class="bow-card-value">Question -> Gemini SQL -> safety check -> BigQuery result</div>
              <div class="bow-card-note">
                Only SELECT and WITH statements are accepted. Write and DDL keywords are rejected before execution.
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    try:
        sql = nl_to_sql(question)
    except Exception as error:
        st.error(f"Gemini is not available: {error}")
        st.info("Set GEMINI_API_KEY, or enable Vertex AI for the Cloud Run service account.")
        return

    error = guard_sql(sql)
    with st.expander("Generated SQL", expanded=True):
        st.code(sql, language="sql")
    if error:
        st.error(error)
        return

    try:
        result = run_sql(sql)
    except Exception as query_error:
        st.error(f"BigQuery rejected the query: {query_error}")
        return

    st.dataframe(result, width="stretch", hide_index=True)
    st.caption(f"{len(result)} rows returned through the read-only query guard.")


def page_gpu() -> None:
    page_glass_header(
        "GPU Acceleration Evidence",
        "Show why large-scale game review analysis needs GPU-speed refreshes for hackathon-scale storytelling.",
        "gpu",
    )
    page_navigation("gpu")
    benchmarks = load_benchmarks()
    end_to_end = benchmarks.loc[benchmarks["stage"] == "End-to-end"].iloc[0]

    cols = st.columns(4)
    cols[0].metric("Dataset scale", "114.4M reviews")
    cols[1].metric("CPU pandas time", f"{end_to_end.pandas_cpu_time:.2f} sec")
    cols[2].metric("GPU cudf.pandas time", f"{end_to_end.cudf_gpu_time:.2f} sec")
    cols[3].metric("End-to-end speedup", f"{end_to_end.speedup:.1f}x")
    st.caption("Measured on the same GCE g2-standard-8 instance: 8 vCPUs with pandas vs NVIDIA L4 with cudf.pandas.")

    table_cols = ["stage", "data_scale", "pandas_cpu_time", "cudf_gpu_time", "speedup"]
    st.dataframe(benchmarks[table_cols], width="stretch", hide_index=True)
    st.plotly_chart(build_benchmark_chart(benchmarks), width="stretch")

    st.markdown("### Time-to-insight")
    st.markdown(
        """
        <div class="bow-panel">
          <div class="bow-card-value">
            GPU acceleration turns full-scale game review analysis from a slow offline batch job into a fast decision system.
          </div>
          <div class="bow-card-note">
            Instead of waiting for a long CPU run, teams can refresh sentiment and bombing signals much faster.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("### Architecture mini diagram")
    architecture_flow()


PAGES = {
    "home": ("Home", page_home),
    "dashboard": ("Decision Demo", page_dashboard),
    "ask": ("Ask BuyOrWait AI", page_ask),
    "alerts": ("Review Bombing Alerts", page_alerts),
    "gpu": ("GPU Acceleration Evidence", page_gpu),
}

route = current_route()

if route == "home":
    inject_home_shell_styles()
else:
    st.markdown(
        """
        <style>
        header[data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="stActionButton"] {
            display: none !important;
        }
        [data-testid="stSidebar"],
        [data-testid="collapsedControl"] {
            display: none !important;
        }
        .block-container {
            max-width: 1280px;
            padding-top: 1.2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

PAGES[route][1]()
