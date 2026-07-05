# BuyOrWait 🎮 — To Buy or Not to Buy

> Steam sentiment intelligence powered by NVIDIA RAPIDS acceleration — overall rating can be misleading; recent weighted sentiment is the truth.

Based on **100M+ Steam reviews**: playtime-weighted + 90-day half-life decay **Purchase Confidence Score**, and rolling z-score based **Bombing Alert**. GPU reduces the full recalculation time from CPU minutes to GPU seconds.

## Architecture

```
Kaggle (100M reviews, 17GB)
   ▼ Direct download via aria2 + convert_to_parquet.py
Cloud Storage (Slim Parquet, no text columns, ~3-4GB)
   ▼
GCE g2-standard-8 (NVIDIA L4) — cudf.pandas batch processing
   Clean → Game×Day Aggregation → Weighted Confidence Score → Bombing Detection → Phase Timings
   ▼
BigQuery: game_daily / game_scores / alerts / benchmark_results
   ▼
Cloud Run — Streamlit (Pure CPU, scales to zero)
   🛒 Purchase Decision | 🚨 Bombing Alert | ⚡ Why GPU
```

## Benchmarks (Same g2-standard-8 instance: 8 vCPUs vs L4 GPU, zero code changes)

<!-- Fill in the figures from benchmark_results.csv after running H7-9 -->

| Phase | pandas (CPU) | cudf.pandas (L4) | Speedup |
|---|---|---|---|
| read_parquet | 1.69s | 0.73s | 2.3x |
| clean_cast | 8.97s | 0.33s | 27.2x |
| daily_groupby | 11.44s | 0.32s | 35.8x |
| weighted_score | 8.69s | 0.74s | 11.7x |
| bomb_detect | 4.82s | 0.16s | 30.1x |
| **end_to_end** | **38.32s** | **2.75s** | **13.9x** |

Hardware: GCE g2-standard-8 (8 vCPUs / 32GB RAM / NVIDIA L4 24GB), see `benchmarks/` for `nvidia-smi` screenshot.

## Reproduction

```bash
# 1. Data (On GPU VM)
python pipeline/convert_to_parquet.py        # Print column names → Edit COLS → Uncomment convert() and rerun

# 2. Run Benchmarks (Same Machine)
python pipeline/pipeline.py cpu
python -m cudf.pandas pipeline/pipeline.py gpu

# 3. Import Results into BigQuery (Tables: steam_intel.game_daily / game_scores / alerts / benchmark_results)
#    Refer to commands in "48-Hour Sprint Guide" H9-12

# 4. App
cd app && pip install -r requirements.txt
GCP_PROJECT=your_project_id streamlit run app.py
```

## Metric Definitions

- **Purchase Confidence Score**: `score = Σ(wᵢ·voteᵢ)/Σ(wᵢ) × 100` where `wᵢ = log(1+playtime_at_review) × exp(−age_days/90)`. Playtime weight filters out "casual" review noise, and the 90-day half-life decay ensures recent sentiment dominates.
- **Bombing Alert**: Daily negative review rate z-score (relative to 30-day rolling average) > 3, and daily review count > 2x of 30-day rolling average (dual conditions to avoid false positives on small sample sizes).

Data Source: Kaggle Steam Reviews (all sourced from public Steam APIs).
