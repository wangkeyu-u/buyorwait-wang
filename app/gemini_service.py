from __future__ import annotations

import os
import re

import pandas as pd
import streamlit as st
from google.cloud import bigquery

from data_loader import DATASET, PROJECT, table


GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
WRITE_KEYWORDS = re.compile(
    r"\b(insert|update|delete|merge|drop|create|alter|truncate|grant|revoke|call|export)\b",
    re.I,
)
SCHEMA_PROMPT = f"""You translate questions about Steam game reviews into BigQuery Standard SQL.

Tables:
1. {table('game_scores')} — appid INT64, game STRING, score FLOAT64,
   raw_pos_rate FLOAT64, recent_pos_rate FLOAT64, n_reviews INT64, recent_n INT64.
2. {table('game_daily')} — appid INT64, date INT64 in epoch nanoseconds,
   n INT64, pos INT64, neg INT64, pos_rate FLOAT64, neg_rate FLOAT64.
3. {table('alerts')} — appid INT64, game STRING, date INT64 in epoch nanoseconds,
   n INT64, neg_rate FLOAT64, z FLOAT64, base_neg_rate FLOAT64.
4. {table('benchmark_results')} — run_ts STRING, mode STRING, stage STRING,
   seconds FLOAT64, rows INT64.

Rules:
- Output exactly one BigQuery Standard SQL SELECT or WITH ... SELECT statement.
- Read-only. Never generate INSERT, UPDATE, DELETE, DDL, scripting, or comments.
- The snapshot ends on 2023-10-30. Interpret relative dates from that date.
- Match game names case-insensitively.
- End with LIMIT 100 unless the question implies a smaller limit.
"""


def guard_sql(sql: str) -> str | None:
    if not re.match(r"^\s*(select|with)\b", sql, re.I):
        return "Generated statement is not a SELECT, so it was not run."
    if WRITE_KEYWORDS.search(sql):
        return "Generated SQL contains a write or DDL keyword, so it was not run."
    return None


@st.cache_data(ttl=600, show_spinner="Gemini is building the query...")
def nl_to_sql(question: str) -> str:
    from google import genai

    key = os.environ.get("GEMINI_API_KEY")
    client = (
        genai.Client(api_key=key)
        if key
        else genai.Client(
            vertexai=True,
            project=PROJECT,
            location=os.environ.get("VERTEX_LOCATION", "global"),
        )
    )
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=f"{SCHEMA_PROMPT}\nQuestion: {question}\nSQL:",
    )
    sql = response.text.strip()
    return re.sub(r"^```(?:sql)?\s*|\s*```$", "", sql, flags=re.I).strip().rstrip(";")


@st.cache_data(ttl=600, show_spinner="Running a guarded BigQuery query...")
def run_sql(sql: str) -> pd.DataFrame:
    config = bigquery.QueryJobConfig(maximum_bytes_billed=1024**3)
    client = bigquery.Client(project=PROJECT)
    return client.query(sql, job_config=config).to_dataframe()


def connection_label() -> str:
    return f"{PROJECT}.{DATASET}"
