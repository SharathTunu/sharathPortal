# Manager Skills Matrix

## Goal
This matrix lists the competencies needed to design, build, operate, and maintain the Manager orchestration platform.

## Core Skill Areas

### Python Systems Engineering
- Build long-running services and watchdog loops.
- Implement robust file/process operations and exception handling.
- Maintain modular scheduling and utility code.

### Data and State Processing
- Use pandas/NumPy for tabular resource and job-state operations.
- Design state transitions for batch/realtime lifecycle management.
- Keep scheduler logic deterministic and idempotent.

### Linux and Runtime Operations
- Work with process lifecycle tools and host-level diagnostics.
- Manage filesystem contracts (metadata roots, temporary files, markers).
- Handle permissions and service execution behavior in production hosts.

### Docker and Container Orchestration
- Understand image/version selection and container discovery.
- Generate and maintain Docker Compose runtime artifacts.
- Debug volume mount and environment wiring issues.

### GPU Infrastructure
- Interpret `nvidia-smi` metrics (utilization, memory, thermal flags).
- Implement capacity-aware placement and safety thresholds.
- Balance throughput with thermal and memory constraints.

### Video and CV Pipeline Fundamentals
- Understand RTSP/video ingestion patterns and stream health checks.
- Work with ROI geometry (lines, polygons, event settings).
- Validate camera and algorithm metadata contracts.

### Configuration and Security
- Define and evolve JSON/CFG schemas.
- Support backward-compatible config loading.
- Handle encrypted inputs (for example, protected stream endpoints).

### Reliability and Operations
- Add health checks, recovery behaviors, and bad-job cleanup.
- Maintain actionable logs and operational diagnostics.
- Build safe fallback behavior under partial failures.

### Testing and Quality
- Write tests for scheduler decisions and edge cases.
- Use fixtures for camera/pipeline permutations.
- Prevent regressions in resource and container management behavior.

## Proficiency Levels by Role

### Backend Scheduler Engineer
- Advanced: Python systems engineering, scheduler state logic.
- Intermediate: pandas/NumPy, Docker operations, Linux runtime.
- Working knowledge: GPU metrics, CV pipeline terminology.

### Platform/MLOps Engineer
- Advanced: Docker lifecycle, deployment, observability, Linux ops.
- Intermediate: GPU capacity planning, process supervision.
- Working knowledge: scheduler internals and config contracts.

### CV/Video Integration Engineer
- Advanced: camera spec parsing, ROI semantics, stream behavior.
- Intermediate: pipeline config integration and artifact generation.
- Working knowledge: container scheduling constraints.

### QA/Validation Engineer
- Advanced: scenario-based test design and regression strategy.
- Intermediate: scheduler lifecycle testing and failure simulation.
- Working knowledge: GPU/container/video processing basics.

## Practical Checklist for New Contributors
- Understand folder contracts under `config`, `metadata`, and `daily_db`.
- Learn the interaction between `resourcePoll`, `cameraPoll`, and `schedulerPoll`.
- Validate changes against both batch and realtime paths.
- Test failure and restart scenarios, not only happy paths.
- Confirm compose and source artifacts are generated correctly.
