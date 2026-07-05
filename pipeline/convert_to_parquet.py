# -*- coding: utf-8 -*-
"""BuyOrWait Step 1: Raw CSV -> Slim Parquet (discard review text, keep only metric columns).

Usage (according to Guide H1-4):
  1. python convert_to_parquet.py          # Only print the actual column names of each CSV
  2. Verify/modify the COLS mapping below
  3. Uncomment convert() at the end of the file, then run again for full conversion
Outputs:
  slim_parquet/part_*.parquet   (metric columns, no text)
  slim_parquet/names.parquet    (appid -> game name mapping, for app display)
Environment variables: RAW_DIR (default: ~/raw), OUT_DIR (default: ./slim_parquet), CHUNK_ROWS (default: 2,000,000)
"""
import glob
import os
import sys
import time

import pandas as pd

RAW_DIR = os.path.expanduser(os.environ.get("RAW_DIR", "~/raw"))
OUT_DIR = os.environ.get("OUT_DIR", "slim_parquet")
CHUNK_ROWS = int(os.environ.get("CHUNK_ROWS", 2_000_000))

# ---- Column mapping: canonical name -> dataset actual column name ----------
# Default guess based on primary option kieranpoc/steam-reviews. Run print mode to verify first!
COLS = {
    "appid": "appid",
    "game": "game",                                    # Game name, only written to names.parquet
    "voted_up": "voted_up",                            # Upvote True / Downvote False
    "votes_up": "votes_up",                            # Review upvote count (backup)
    "playtime_at_review": "author_playtime_at_review", # Playtime in minutes at review time
    "timestamp_created": "timestamp_created",          # Unix timestamp in seconds
}
# Downgrade dataset najzeko/steam-reviews-2021 uses this mapping (uncomment to override above):
# COLS = {
#     "appid": "app_id",
#     "game": "app_name",
#     "voted_up": "recommended",
#     "votes_up": "votes_helpful",
#     "playtime_at_review": "author.playtime_at_review",
#     "timestamp_created": "timestamp_created",
# }
# -----------------------------------------------------------------------------


def csv_files():
    files = sorted(glob.glob(os.path.join(RAW_DIR, "**", "*.csv"), recursive=True))
    if not files:
        sys.exit(f"[!] No CSV files found under {RAW_DIR}. Please confirm download/extraction is complete.")
    return files


def print_columns():
    """Print actual column names to verify the COLS mapping."""
    for f in csv_files():
        head = pd.read_csv(f, nrows=5)
        size_gb = os.path.getsize(f) / 1e9
        print(f"\n=== {f} ({size_gb:.1f} GB) ===")
        for c in head.columns:
            print(f"  {c!r:45s} Example: {head[c].iloc[0]!r}")
    print("\n[√] Once column names are verified with the COLS mapping, uncomment convert() at the end of the file and run again for the full conversion.")


def _norm_bool(s: pd.Series) -> pd.Series:
    """Normalize True/False/'true'/'False'/1/0 into int8."""
    if s.dtype == bool:
        return s.astype("int8")
    return (
        s.astype(str).str.strip().str.lower()
        .map({"true": 1, "false": 0, "1": 1, "0": 0})
        .astype("float32")  # Keep NaN temporarily, discard during cleaning
    )


def convert():
    os.makedirs(OUT_DIR, exist_ok=True)
    usecols = list(COLS.values())
    rename = {v: k for k, v in COLS.items()}
    names: dict = {}          # appid -> game name mapping
    part, total = 0, 0
    t0 = time.time()

    for f in csv_files():
        try:
            reader = pd.read_csv(
                f, usecols=usecols, chunksize=CHUNK_ROWS,
                on_bad_lines="skip", low_memory=True,
            )
        except ValueError as e:
            sys.exit(f"[!] {f} column names mismatch: {e}\n    Run print mode first, and adjust COLS.")

        for chunk in reader:
            df = chunk.rename(columns=rename)

            # Collect appid -> game mapping and drop text columns
            pairs = df[["appid", "game"]].dropna().drop_duplicates("appid")
            names.update(dict(zip(pairs["appid"], pairs["game"])))
            df = df.drop(columns=["game"])

            # Types and cleaning
            df["voted_up"] = _norm_bool(df["voted_up"])
            for c in ("appid", "votes_up", "playtime_at_review", "timestamp_created"):
                df[c] = pd.to_numeric(df[c], errors="coerce")
            df = df.dropna(subset=["appid", "voted_up", "timestamp_created"])
            df = df.astype({
                "appid": "int32", "voted_up": "int8",
                "timestamp_created": "int64",
            })
            df["votes_up"] = df["votes_up"].fillna(0).astype("int32")
            df["playtime_at_review"] = df["playtime_at_review"].fillna(0).astype("float32")

            df.to_parquet(f"{OUT_DIR}/part_{part:04d}.parquet", index=False)
            total += len(df)
            print(f"  part_{part:04d}  +{len(df):>9,} rows  total {total:>12,}  "
                  f"{time.time() - t0:6.0f}s", flush=True)
            part += 1

    pd.DataFrame({"appid": list(names.keys()), "game": list(names.values())}) \
        .astype({"appid": "int32"}) \
        .to_parquet(f"{OUT_DIR}/names.parquet", index=False)
    print(f"\n[√] Finished: {total:,} rows -> {part} part files + names.parquet ({len(names):,} games)")
    print(f"    Next step: gsutil -m cp -r {OUT_DIR} gs://buyorwait-data/")


if __name__ == "__main__":
    print_columns()
    # convert()   # <- Uncomment this line to run full conversion after verifying column names
