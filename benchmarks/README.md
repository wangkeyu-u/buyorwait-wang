# Benchmarks ⚡

This directory contains the dual-run benchmark results comparing CPU vs. GPU data processing pipelines for BuyOrWait.

## Summary of Results

The pipeline processes **114,381,811** Steam review records on the same Google Compute Engine (GCE) `g2-standard-8` instance, contrasting `pandas` (CPU baseline) with `cudf.pandas` (GPU acceleration with zero code changes).

| Phase | pandas (CPU) | cudf.pandas (L4 GPU) | Speedup |
| :--- | :---: | :---: | :---: |
| `read_parquet` | 1.69s | 0.73s | 2.3x |
| `clean_cast` | 8.97s | 0.33s | 26.9x |
| `daily_groupby` | 11.44s | 0.32s | 35.7x |
| `weighted_score` | 8.69s | 0.74s | 11.8x |
| `bomb_detect` | 4.82s | 0.16s | 30.7x |
| `write_outputs` | 2.72s | 0.47s | 5.8x |
| **`end_to_end`** | **38.32s** | **2.75s** | **~14x** |

## Contents of This Directory

- [benchmark_results.csv](benchmark_results.csv): Raw timestamped output appended by `pipeline.py` during CPU and GPU runs.
- `nvidia-smi.png`: Screenshot verifying GPU usage on the GCE L4 machine (concrete proof of GCP × NVIDIA integration).

## Hardware Specifications

- **Instance Type**: GCP GCE `g2-standard-8`
- **CPU**: 8 vCPUs / 32 GB RAM
- **GPU**: NVIDIA L4 (24 GB VRAM)
- **OS**: Ubuntu 24.04 LTS (Deep Learning Image)
- **CUDA Version**: 12.x / Driver 580+
