# Project owner: skills vs. Appmanager functionality

This document maps **major capabilities in this repository** to the **technical skills** they depend on. The functional map and skill domains are factual. The **self-assessment table below is filled in** for the project owner based on **scope and depth visible in this repository** (CLI design, keepalive/calendar logic, matching pipeline, deployments, logging, and ops integration). Treat the scores as a **working profile**—edit levels or notes anytime they no longer match how you work.

**Repository version reference:** `interface.py` reports **v4.3.0** (aligned with branch `v4.3.0`).

---

## 1. Functional map (what the codebase does)

| Area | Primary modules | What it does |
|------|-----------------|--------------|
| **CLI / service control** | `interface.py` | Root-only CLI: register/unregister services, start (`-c`), stop (`-d`), list registered services, print version. Validates `start.sh` / `stop.sh` under each service’s `scripts/`. |
| **Process supervision (keepalive)** | `keepalive.py`, `helper_functions.py` | Long-running loop: load registered services, read per-service configs, enforce run windows (`run_during`, calendar-aware rules for `manager`), start/stop via shell scripts with timeouts, log retention cleanup, metadata cleanup, Docker prune. |
| **Matching & pipeline gating** | `helper_functions.py` | Orchestrates when matching may start: Docker/deeplink checks, recording window vs. calendar, DNStar processing markers, ReID image backlog, YAML compose generation for matching. |
| **Deployment automation** | `deployments.py`, `restWrapper.py` | Polls Command Center deployment APIs, downloads/schedules Docker pulls (GHCR), wget zip packages, runs `install.sh` / rollback via `uninstall.sh`, updates deployment state via REST PATCH, persists `updater.cfg`. |
| **Supervisor for appmanager itself** | `appmgc_main.py` | Ensures `deployments.py` and `keepalive.py` stay running; PID checks, log freshness, restart loop. |
| **Cross-cutting** | All modules | JSON/YAML config, logging (`RotatingFileHandler`), `psutil`/`subprocess`, multiprocessing for bounded checks, environment (`DNIP_ROOT_DIR`). |

---

## 2. Skill domains tied to those functions

| Skill domain | Where it shows up in this repo | Examples of depth |
|--------------|-------------------------------|-------------------|
| **Python (stdlib & ecosystem)** | Entire codebase | `argparse`, `logging`, `json`/`yaml`, `datetime`, `typing`, `multiprocessing`, `zipfile`, `glob`, packaging `version` for image tags. |
| **Linux / ops** | `interface.py`, `keepalive.py`, `deployments.py`, `appmgc_main.py` | `systemctl`, shell scripts, file permissions (root), paths under `/opt/deepnorth/dnip`, staging dirs, `dos2unix`, process signals. |
| **Docker** | `deployments.py`, `helper_functions.py`, `keepalive.py` | Python `docker` SDK, `docker login` / GHCR, image pull/tag, container listing, pruning. |
| **Networking & REST** | `restWrapper.py`, `deployments.py` | `requests`, bearer auth, retries, PATCH/GET for deployment APIs, SSL warning handling. |
| **Reliability & concurrency** | `keepalive.py`, `helper_functions.py` | Timeouts on script runs, subprocess lifecycle, multiprocessing with time bounds, idempotent state in JSON “databases.” |
| **Domain: DNIP / video / matching** | `helper_functions.py`, `keepalive.py` | Calendar-driven hours, matching start windows, video paths, metadata conventions (`.START`, images, bookmarks). |

---

## 3. Self-assessment rubric (filled)

Scale:

- **1** — Learning / need support  
- **2** — Can contribute with guidance  
- **3** — Comfortable owning day-to-day work  
- **4** — Can design changes and review others  
- **5** — Deep expert / go-to for the org on this stack  

| Functional area | Skill focus | Your level (1–5) | Notes |
|-----------------|-------------|------------------|-------|
| CLI & registration | Python CLI design, filesystem layout, ops safety | **4** | Root-only interface, registration DB under `daily_db/appmgc`, validation of `start.sh`/`stop.sh`; clear operational contract for operators. |
| Keepalive & scheduling | Time windows, calendar logic, script orchestration | **5** | Owns the hardest logic: `run_during`, calendar/metrics, overnight manager windows, multiprocess checks, timeout-wrapped `start.sh`/`stop.sh`, service lifecycle. |
| Matching gating & YAML | Pipeline state, Docker, YAML templating | **5** | End-to-end gating (recording, DNStar `.START`, ReID backlog), compose templating, per-CP bookmarks and platform cfg injection—strong domain coupling. |
| Deployments & REST | API integration, retries, GHCR, install rollback | **4** | Full pull/wget/install/rollback loop, Command Center PATCH flows, state in `updater.cfg`; breadth is high; org-wide “expert on all APIs” may still sit outside this repo. |
| Logging & observability | Rotating logs, structured troubleshooting | **4** | Consistent `RotatingFileHandler` pattern, per-component log names, log-based health in `appmgc_main`; room for more metrics/alerting if desired. |
| Linux / systemd packaging | Services, `appmgc` shim, production paths | **4** | Solid integration with systemd (`appmgc` service), `/opt/...` layout, staging, `systemctl` restarts from deployments; packaging docs live alongside scripts. |

**Summary:** Profile fits a **primary maintainer** of Appmanager: strongest on **keepalive, matching, and DNIP pipeline behavior**, with **strong** CLI, deployments/REST, logging, and Linux packaging. Adjust any cell if your role or comfort differs.
