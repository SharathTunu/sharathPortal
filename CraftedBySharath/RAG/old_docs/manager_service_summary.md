# Manager Executive Summary

## What this system is
`Manager` is a Python orchestration service for GPU-based video analytics. It keeps core services alive, tracks GPU capacity, interprets camera and algorithm configs, and controls batch/realtime analytics containers.

## What it does in production
- Supervises core polling and scheduling services and restarts them when unhealthy.
- Monitors GPU health (utilization, memory, temperature, thermal throttling) for placement decisions.
- Interprets camera configs to decide processing mode and run windows.
- Generates source/ROI artifacts and per-workload Docker Compose files.
- Starts/stops analytics workloads based on resource availability and scheduling rules.
- Controls DeepSense lifecycle using backlog and time-window policies.

## Why it matters
- Maximizes GPU utilization while protecting runtime stability.
- Keeps realtime processing responsive while coordinating batch throughput.
- Converts config changes into deterministic runtime behavior.
- Reduces manual operations through automated health recovery and scheduling.

## Technical profile
- Stack: Python, pandas/NumPy, OpenCV, Docker SDK, Linux process/file operations.
- Runtime dependencies: NVIDIA GPUs (`nvidia-smi`), Docker/Compose, structured config roots.
- Reliability mechanisms: rolling logs, health checks, marker files, bad-job cleanup.

## Skills needed to build and maintain
- Python backend engineering for schedulers and system processes.
- MLOps/DevOps for container lifecycle, deployment, and observability.
- CV/video pipeline knowledge for RTSP/video ingestion and ROI semantics.
- GPU operations knowledge for capacity-aware orchestration.
- QA/test engineering for scheduler edge cases and regression prevention.

## Suggested ownership model
- Backend owner: scheduler, config, and orchestration logic.
- Platform owner: Docker/GPU runtime operations and deploy tooling.
- CV owner: ROI generation and algorithm integration behavior.
- QA owner: scenario-based tests across batch/realtime and failure paths.
