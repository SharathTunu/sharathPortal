# Project owner: skills vs. codebase functionality

**Purpose:** Map the camera recorder codebase to the technical competencies it involves, and record **your** proficiency against each area. Update the self-rating column whenever your skills change.

**Primary maintainer (git history):** Sharath Tunu / Sharath Tunuguntla — majority of commits; additional contributions from teammates (e.g. alert publisher authorship, shared modules).

---

##Rrating scale

| Level | Meaning |
| ----- | ------- |
| **0** | Not applicable / delegated |
| **1** | Awareness — can follow docs or pair with someone |
| **2** | Working — can implement or debug with reference material |
| **3** | Proficient — routine ownership without heavy support |
| **4** | Strong — designs changes, handles edge cases, mentors others |
| **5** | Expert — deep domain authority; drives standards in this area |

---

## Core runtime: RTSP recording and process orchestration

| Functionality (where in repo) | Competencies | Evidence in this codebase | Your rating |
| ------------------------------- | ------------ | ------------------------- | ----------- |
| Per-camera launcher scripts, start/stop orchestration (`src/rtsp_recorder.py`, `/launchers`) | Python, process lifecycle, shell integration | `VideoCaptureStatus`: compares running vs expected launchers, moves stale scripts to `remove`, regenerates on camera update | **4** |
| FFmpeg command construction from templates (`src/ffmpeg_script_generator.py`, `config/ffmpegs.json`) | FFmpeg CLI, RTSP (`-rtsp_transport tcp`), segment mux, path/layout rules | String templates for `video_unencrypted`, `video_segmentation`, `video_encrypted`; CENC-style encryption flags in JSON | **4** |
| Camera model: host, timezone, schedule, capture interval (`src/cameras.py`) | OpenCV `VideoCapture`, `zoneinfo`, time windows | `is_processing_hours` with buffer; per-camera timezone; `valid_rtsp` | **4** |
| Calendar / Command Center hours (`src/rtsp_recorder.py` — `calendar.json`) | JSON config integration, date logic | Reads `dailyStartAt` / `dailyEndAt` and per-day metrics | **4** |

---

## Configuration and platform integration

| Functionality | Competencies | Evidence in this codebase | Your rating |
| ------------- | ------------ | ------------------------- | ----------- |
| Central config loading (`src/config.py`, `config/camera_recorder.cfg`) | JSON/binary config, env vars (`DNIP_ROOT_DIR`), platform paths | Binary-to-JSON fallback reader; merges `platform.cfg` for `video_root`; feature flags (`SEG_REC`, `IS_VERKADA_ENABLED`) | **5** |
| Recording modes: unencrypted / encrypted / re-encode subsets (`config.py`, `camera_recorder.cfg`) | Multi-tenant or multi-mode ops design | Lists like `unencrypted`, `encrypted`, `re_encode_cams`, `re_encrypt_videos` | **4** |
| Docker / deployment (`scripts/camera_recorder_compose.yml`) | Docker Compose, host networking, GPU env, volume mounts | `network_mode: host`, NVIDIA vars, bind mounts for config and `/videos` | **4** |

---

## Security and data handling

| Functionality | Competencies | Evidence in this codebase | Your rating |
| ------------- | ------------ | ------------------------- | ----------- |
| Stream URL encryption (`src/helpers.py` — `encrypt_str` / `decrypt_str`) | AES-CBC, padding, base64/hex handling | PyCryptodome-style AES usage with default key override via config | **3** |
| Verkada JWT flow (`src/get_token.py`, `config` when Verkada enabled) | REST APIs, retries, backoff, atomic file writes | `requests`, exponential backoff, `tempfile` + `os.replace` for JWT file | **4** |

---

## Post-processing: quality, re-encode, GPU parallelism

| Functionality | Competencies | Evidence in this codebase | Your rating |
| ------------- | ------------ | ------------------------- | ----------- |
| Deep video diagnostics (`src/diagnose_video.py`) | `ffprobe`/FFmpeg error analysis, typing, structured logging | Codec info, frame error scan, PTS/DTS, keyframes, VFR — documented in module docstring | **4** |
| Re-encode / repair pipeline (`src/re_encoder.py`) | `ffmpeg`/`ffprobe` subprocess, concurrency (`ThreadPoolExecutor`), pandas, signals | Uses `diagnose_video`; GPU process limits; reloadable config; `fix_start_time` patterns | **4** |
| Kill / overrun scripts (`scripts/kill_ffmpeg_overrun.py`) | Ops scripting, process hygiene | Supporting operational script | **4** |

---

## Observability and cloud alerts

| Functionality | Competencies | Evidence in this codebase | Your rating |
| ------------- | ------------ | ------------------------- | ----------- |
| FPS / alerting → Google Pub/Sub (`src/alert_publisher.py`, `config/cc_alerts.json`) | GCP Pub/Sub, credentials, JSON alert payloads | `PublishClient_alerts`; scans `fps_alert_*.json`; `reorder_dict` schema | **3** |
| Logging (`src/helpers.py` — `init_log`) | Python `logging`, rotating files | Shared pattern across services | **4** |

---

## Summary snapshot (optional)

Use this one-line summary for CVs, reviews, or onboarding docs (edit freely).

| Domain | One-line statement (your words) |
| ------ | -------------------------------- |
| Python services | Proficient-strong owner (`5`): I can design, debug, and maintain end-to-end recorder services independently. |
| FFmpeg / video | Strong (`4`): I handle recording modes, segmentation, and repair flows with practical production troubleshooting. |
| Cloud (GCP) / networking | Proficient (`4`): I can operate and extend Pub/Sub based alert integrations with references when needed. |
| Security / crypto | Working-proficient (`4`): I can maintain current encryption/token mechanisms and safely evolve them. |
| Containers / Linux ops | Strong (`5`): I can deploy, tune, and operate the service stack on host/GPU-based environments. |

