from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
import streamlit as st
from google.cloud import bigquery


APP_DIR = Path(__file__).parent
PROJECT = os.environ.get("GCP_PROJECT", "buyorwait-2026")
DATASET = os.environ.get("BQ_DATASET", "steam_intel")
DATA_MODE = os.environ.get("BUYORWAIT_DATA_MODE", "auto").lower()


def table(name: str) -> str:
    return f"`{PROJECT}.{DATASET}.{name}`"


@st.cache_resource
def _client() -> bigquery.Client:
    return bigquery.Client(project=PROJECT)


@st.cache_data(ttl=600, show_spinner=False)
def _query(sql: str, params: tuple[tuple[str, str, object], ...] = ()) -> pd.DataFrame:
    config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(name, kind, value)
            for name, kind, value in params
        ]
    )
    return _client().query(sql, job_config=config).to_dataframe()


def _query_or_none(sql: str, params: tuple[tuple[str, str, object], ...] = ()) -> pd.DataFrame | None:
    if DATA_MODE == "demo":
        return None
    try:
        return _query(sql, params)
    except Exception:
        if DATA_MODE in {"bigquery", "production"}:
            raise
        return None


def _demo_csv(name: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(APP_DIR / "mock_data" / name, **kwargs)


@st.cache_data(ttl=600)
def load_game_scores() -> pd.DataFrame:
    rows = _query_or_none(
        f"""
        SELECT appid, game, score, raw_pos_rate, recent_pos_rate, n_reviews, recent_n
        FROM {table('game_scores')}
        ORDER BY n_reviews DESC
        LIMIT 10000
        """
    )
    if rows is None or rows.empty:
        return _demo_csv("game_scores.csv", parse_dates=["last_updated"])

    recent = rows["recent_pos_rate"].fillna(rows["raw_pos_rate"]).astype(float)
    delta = (rows["raw_pos_rate"].astype(float) - recent) / 100
    signal = pd.cut(
        delta,
        bins=[-float("inf"), 0.05, 0.10, 0.20, float("inf")],
        labels=["Clear", "Watch", "Elevated", "Critical"],
        right=False,
    ).astype(str)
    return pd.DataFrame(
        {
            "game_name": rows["game"].fillna("Unknown game"),
            "appid": rows["appid"].astype("int64"),
            "genre": "Steam title",
            "review_count": rows["n_reviews"].fillna(0).astype("int64"),
            "last_updated": pd.Timestamp("2023-10-30"),
            "buy_confidence_score": rows["score"].fillna(0).astype(float),
            "recent_positive_rate": recent / 100,
            "review_volume_30d": rows["recent_n"].fillna(0).astype("int64"),
            "negative_rate_change": delta,
            "weighted_confidence_score": rows["score"].fillna(0).astype(float),
            "bombing_signal": signal,
        }
    )


def get_game_names() -> list[str]:
    scores = load_game_scores()
    return scores.sort_values(["review_count", "game_name"], ascending=[False, True])["game_name"].tolist()


def get_game_score(game_name: str) -> pd.Series:
    scores = load_game_scores()
    return scores.loc[scores["game_name"] == game_name].iloc[0]


@st.cache_data(ttl=600)
def get_daily_for_game(game_name: str) -> pd.DataFrame:
    game = get_game_score(game_name)
    rows = _query_or_none(
        f"""
        SELECT
          DATE(TIMESTAMP_SECONDS(DIV(date, 1000000000))) AS date,
          n AS review_volume,
          pos_rate AS positive_rate,
          1 - pos_rate AS negative_rate
        FROM {table('game_daily')}
        WHERE appid = @appid
        ORDER BY date
        """,
        (("appid", "INT64", int(game.appid)),),
    )
    if rows is None or rows.empty:
        daily = _demo_csv("daily_stats.csv", parse_dates=["date"])
        return daily.loc[daily["game_name"] == game_name].sort_values("date")
    rows["date"] = pd.to_datetime(rows["date"])
    rows["game_name"] = game_name
    rows["appid"] = int(game.appid)
    return rows


@st.cache_data(ttl=600)
def load_alerts() -> pd.DataFrame:
    rows = _query_or_none(
        f"""
        SELECT
          game,
          appid,
          DATE(TIMESTAMP_SECONDS(DIV(date, 1000000000))) AS alert_date,
          neg_rate,
          base_neg_rate,
          LEAST(z, 99.9) AS z,
          n
        FROM {table('alerts')}
        ORDER BY date DESC, n DESC
        LIMIT 1000
        """
    )
    if rows is None or rows.empty:
        return _demo_csv("alerts.csv", parse_dates=["alert_date"])

    rows["alert_date"] = pd.to_datetime(rows["alert_date"])
    severity = pd.cut(
        rows["z"].astype(float),
        bins=[-float("inf"), 4.0, 6.0, float("inf")],
        labels=["Medium", "High", "Critical"],
        right=False,
    ).astype(str)
    return pd.DataFrame(
        {
            "game_name": rows["game"].fillna("Unknown game"),
            "appid": rows["appid"].astype("int64"),
            "alert_date": rows["alert_date"],
            "negative_rate": rows["neg_rate"].astype(float),
            "rolling_30d_negative_rate": rows["base_neg_rate"].astype(float),
            "z_score": rows["z"].astype(float),
            "review_volume": rows["n"].fillna(0).astype("int64"),
            "volume_multiplier": (2 + rows["z"].astype(float) / 10).round(1),
            "severity": severity,
            "possible_reason": "Negative sentiment and review volume spiked above the 30-day baseline",
        }
    )


def get_alert_window(game_name: str, alert_date: pd.Timestamp, days: int = 21) -> pd.DataFrame:
    daily = get_daily_for_game(game_name).copy()
    start = alert_date - pd.Timedelta(days=days)
    end = alert_date + pd.Timedelta(days=days)
    return daily.loc[(daily["date"] >= start) & (daily["date"] <= end)]


def _normalise_benchmarks(rows: pd.DataFrame) -> pd.DataFrame:
    latest = rows.sort_values("run_ts").groupby(["mode", "stage"], as_index=False).last()
    pivot = latest.pivot(index="stage", columns="mode", values="seconds")
    row_counts = latest.groupby("stage")["rows"].max()
    stages = {
        "read_parquet": "Read Parquet",
        "clean_cast": "Clean + Type Conversion",
        "daily_groupby": "Groupby Daily Aggregation",
        "weighted_score": "Weighted Score Calculation",
        "bomb_detect": "Rolling Window Bombing Detection",
        "write_outputs": "Write Outputs",
        "end_to_end": "End-to-end",
    }
    records = []
    for key, label in stages.items():
        if key not in pivot.index:
            continue
        cpu = float(pivot.loc[key, "cpu"]) if "cpu" in pivot.columns else float("nan")
        gpu = float(pivot.loc[key, "gpu"]) if "gpu" in pivot.columns else float("nan")
        records.append(
            {
                "stage": label,
                "data_scale": f"{int(row_counts.get(key, 0)):,} reviews",
                "pandas_cpu_time": cpu,
                "cudf_gpu_time": gpu,
                "speedup": cpu / gpu if gpu else float("nan"),
            }
        )
    return pd.DataFrame.from_records(records)


@st.cache_data(ttl=600)
def load_benchmarks() -> pd.DataFrame:
    rows = _query_or_none(f"SELECT run_ts, mode, stage, seconds, rows FROM {table('benchmark_results')}")
    if rows is None or rows.empty:
        local = APP_DIR.parent / "benchmarks" / "benchmark_results.csv"
        if local.exists():
            rows = pd.read_csv(local)
    if rows is None or rows.empty:
        return _demo_csv("benchmark_results.csv")
    return _normalise_benchmarks(rows)
