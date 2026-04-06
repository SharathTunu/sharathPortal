# Skills profile vs. matching QA tool functionality

This document maps **major areas of the codebase** to the **technical skills they involve**, and now reflects the profile of an engineer who **built the full project end-to-end**.

**Skill level scale (for the tables below)**

| Level | Meaning |
|-------|---------|
| **L1 — Awareness** | Understand concepts; need guidance to implement. |
| **L2 — Working** | Can implement with docs or occasional help. |
| **L3 — Proficient** | Own features end-to-end; debug and extend confidently. |
| **L4 — Strong** | Guide others; shape design; handle edge cases and performance. |

---

## 1. Streamlit QA application (`main.py`)

**What the tool does**

- Loads matching zone records and images for a selected date; optional MZR-only vs MZR + unmatched workflows.
- Filters by time range, zone (global vs zone mode), track type (entry/exit/both), object ID, and unique vs all tracks.
- Renders paginated image grids with metadata (zone, camera, line, object, timestamps).
- Supports duplicate object ID reassignment, employee vs customer flags, cluster “not matching” removal, and manual entry–exit pairing for unmatched data.
- Integrates dwell-time calculation trigger and CSV download; save/load session state.

**Skills involved**

- Streamlit: layout (`st.columns`, containers), `session_state`, widgets, callbacks (`on_click`, `on_change`), forms, spinners.
- Stateful UI design and validation logic (e.g. one entry paired with one exit, zone and time constraints).

**Self-assessment (project owner profile)**

| Skill / topic | Level (L1–L4) | Notes (optional) |
|---------------|---------------|------------------|
| Streamlit apps & session state | L4 | Built complete stateful review workflow and maintained UX consistency across reruns. |
| Multi-column layouts & pagination UX | L4 | Designed dual-panel query/match views and pagination for analyst-scale review sessions. |
| Callbacks and form workflows | L4 | Implemented `on_click`/`on_change` interactions, forms, and validation for safe user actions. |

---

## 2. Data loading, filtering, and image linkage (`utils.py`, `generate_csv.py`)

**What the code does**

- Reads `matching_zone_records.csv`, normalizes timestamps, and maps rows to image files by building an indexed structure from filenames (camera, line, track, entry flag).
- Regex-based parsing for multiple timestamp filename formats (`TS...` patterns).
- Filters DataFrames by time, zone, object ID, track type; fetches query image details for the UI.
- Unmatched image discovery via glob vs matched set; enriches unmatched rows using `zone_line_map` and synthetic track IDs.
- OpenCV-based image read/resize for previews; optional PIL usage in `main.py` for display.

**Skills involved**

- **pandas**: filtering, `groupby`, datetime handling, string extract, merge/map with zone metadata.
- **Python**: `glob`, path handling, iterators (`itertools.islice` for pagination helper).
- **Image pipelines**: filename conventions, joining algorithm output to filesystem assets.

**Self-assessment (project owner profile)**

| Skill / topic | Level (L1–L4) | Notes (optional) |
|---------------|---------------|------------------|
| pandas (filter, merge, time series) | L4 | Built filtering and transformation pipeline used across matching and unmatched flows. |
| File indexing / regex on paths | L4 | Implemented filename parsing and image-to-record mapping with mixed timestamp formats. |
| OpenCV / image loading | L3 | Implemented image loading/resizing pipeline for UI display and QA navigation. |

---

## 3. Dwell time analytics (`dwell_time_calculator.py`)

**What the code does**

- Merges matched PMR data with successfully matched unmatched records.
- Per-zone processing: groups by `object_id`, walks ordered events, pairs entry→exit transitions into dwell segments.
- Outputs a structured DataFrame for CSV export (zone name, times, dwell duration, employee flag).

**Skills involved**

- Domain logic for retail/vision “matching records” and dwell semantics.
- Event ordering, grouping, and careful iteration over heterogeneous tracks.

**Self-assessment (project owner profile)**

| Skill / topic | Level (L1–L4) | Notes (optional) |
|---------------|---------------|------------------|
| Analytics on grouped time-series events | L4 | Built per-zone dwell computation and entry/exit pairing logic for production outputs. |
| Translating product rules into code | L4 | Encoded QA constraints (zone/time/order validity, match semantics, employee handling). |

---

## 4. Configuration, persistence, logging

**What the code does**

- `config.yml`: image, results, and DB (zone CSV) paths for containerized mounts.
- `logging` to file under `logs/`; module-level loggers.
- Session backup via **pickle** of selected `session_state` keys (`save_session` / `load_session`).

**Skills involved**

- YAML configuration and 12-factor style path overrides.
- Operational logging; understanding Streamlit session persistence limits and workarounds.

**Self-assessment (project owner profile)**

| Skill / topic | Level (L1–L4) | Notes (optional) |
|---------------|---------------|------------------|
| YAML / env-style configuration | L4 | Structured path-driven config model for reproducible execution across environments. |
| Logging practices | L3 | Added actionable logging for data loading, session actions, and error diagnosis. |
| Session persistence trade-offs | L4 | Designed save/load state strategy for long-running QA sessions and recovery workflows. |

---

## 5. Containerization and run automation

**What the repo provides**

- `docker-compose.yml`: Streamlit entrypoint, host networking, volume mounts for images, results, zone DB, timezone.
- `scripts/run.sh`: conditional container start, volume binds, image tag; also includes **vLLM** serve for `Qwen/Qwen3-VL-8B-Instruct`, TensorRT `trtexec` engine builds, `pip install vllm`, and **Wasabi S3** sync of `mzr` data—reflecting deployment and ML-serving concerns beyond the core Streamlit app.

**Skills involved**

- Docker run/compose, volume mapping, reproducible runs.
- Optional: GPU model serving (vLLM), object storage sync, TensorRT (environment-specific).

**Self-assessment (project owner profile)**

| Skill / topic | Level (L1–L4) | Notes (optional) |
|---------------|---------------|------------------|
| Docker & bind mounts | L4 | Built containerized runtime with host networking, data mounts, and operational defaults. |
| Shell scripting for deploy | L4 | Implemented startup automation, lifecycle checks, and environment-path wiring. |
| vLLM / VL model serving | L3 | Integrated model-serving commands and runtime provisioning for vision-language workflows. |
| Cloud object storage (S3-compatible) | L3 | Added artifact sync path to Wasabi for workflow data movement and archival. |
| TensorRT / ONNX engines | L3 | Added reproducible `trtexec` commands for engine build and verification workflows. |

---

## 6. Planned or adjacent work (not fully in-repo)

- **`main.py`** contains comments about **Gemini** verification for match clusters; implementation is not present in the snippet reviewed—suggests roadmap for LLM-assisted QA.
- **`qwen/`** is listed in `.gitignore`; related evaluation or outputs may live outside version control and are treated as part of your broader project ownership.

---

## Summary checklist (quick CV alignment)

Use this list to align résumé or interview talking points with the codebase:

- [x] End-to-end **Streamlit** tool for **ReID / matching QA** with rich **session state** and **CSV export**.
- [x] **pandas**-centric ETL from algorithm outputs + **filesystem** image linkage.
- [x] **Dwell time** and **entry/exit** business logic.
- [x] **Docker**-based delivery with **vLLM**, **S3**, and **TensorRT** workflows in run path.
- [x] **Logging**, **YAML config**, and **session backup** for long review sessions.

