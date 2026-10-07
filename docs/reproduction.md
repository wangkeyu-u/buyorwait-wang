# 重建上游管线

这些步骤对应保留的上游代码；本 fork 没有执行全量数据或 GPU/云端重建。

## Python 环境与数据转换

从仓库根目录创建虚拟环境，安装应用中声明的 pandas、pyarrow 及云端依赖：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
```

自行取得有权使用的 Steam CSV，放在 `RAW_DIR`（默认 `~/raw`）。先核对实际列与 `pipeline/convert_to_parquet.py` 的 `COLS`：

```bash
RAW_DIR=/path/to/csv python pipeline/convert_to_parquet.py
```

当前脚本默认只打印列。确认映射后，在脚本末尾启用 `convert()` 才会执行转换；产物默认写入 `slim_parquet/part_*.parquet` 和 `names.parquet`。原始数据不入库。

## CPU 与 GPU

```bash
MAX_FILES=3 python pipeline/pipeline.py cpu
python pipeline/pipeline.py cpu
```

`DATA_DIR` 可覆盖 Parquet 输入目录，输出为根目录的 `out_*.parquet` 与追加式 `benchmark_results.csv`。生成的 CSV 是本次运行记录，不是 `benchmarks/` 中的历史记录。

GPU 需要另行安装与 CUDA/驱动匹配的 RAPIDS/cuDF 环境；应用 requirements 没有提供该环境：

```bash
python -m cudf.pandas pipeline/pipeline.py gpu
```

同一数据、硬件、软件版本和测量方法下的独立计时，才可用于新的加速比结论。

## 云端应用

Streamlit 从 BigQuery 的 `game_daily`、`game_scores`、`alerts` 和 `benchmark_results` 读取聚合结果。先在自己的项目中建立并装载这些表，配置 Google Cloud 身份，再运行：

```bash
GCP_PROJECT=your_project_id BQ_DATASET=steam_intel streamlit run app/app.py
```

可选 Gemini 通过 `GEMINI_API_KEY` 或 Vertex AI 服务账号调用，模型由 `GEMINI_MODEL` 配置。查看[上游 Looker 说明](looker_studio.md)和[SQL views](looker_views.sql)获取相关表/视图配置。不要将上游展示URL理解为本fork部署。
