# My Skill Level Against Codebase Functionalities

## Context

This document maps my current skill level to the major functionalities in the `matching` codebase.  
Assessment scale used:

- **L1 - Basic**: can use with support
- **L2 - Working**: can implement small changes independently
- **L3 - Proficient**: can design and deliver features end-to-end
- **L4 - Advanced**: can optimize, troubleshoot deeply, and mentor others
- **L5 - Expert**: defines architecture and standards across systems

## Functionality-to-Skill Mapping

### 1. Configuration-Driven Execution

- **Functionality**: manage behavior via `configs/matching.yml` and config loaders.
- **My Level**: **L4 - Advanced**
- **Evidence of capability**:
  - understand and tune runtime flags for matching flow, parallelism, and output behavior
  - trace config effects across modules and troubleshoot bad parameter combinations
  - support environment-specific config updates safely

### 2. Input Validation and Job Lifecycle

- **Functionality**: validate runtime inputs, initialize logs, and handle start/finish/error status.
- **My Level**: **L4 - Advanced**
- **Evidence of capability**:
  - understand job lifecycle in `matching/main.py`
  - diagnose startup failures and validation breaks quickly
  - ensure status events and log states remain consistent during failures

### 3. DB CSV Ingestion and Zone Mapping

- **Functionality**: load zone tables and generate line-to-zone mappings.
- **My Level**: **L3 - Proficient**
- **Evidence of capability**:
  - can maintain and update ingestion logic in `matching/db/db_operation.py`
  - understand property/camera/other/conversion zone classification rules
  - can debug malformed or partial CSV inputs

### 4. Feature Loading and Preprocessing

- **Functionality**: read/filter/normalize `.npy` features and align PMR metadata.
- **My Level**: **L4 - Advanced**
- **Evidence of capability**:
  - can tune parallel read settings and timestamp filtering logic
  - can handle edge cases (corrupt files, missing fields, ordering/alignment issues)
  - understand feature normalization trade-offs and downstream impact

### 5. Matching Orchestration

- **Functionality**: coordinate property, dwell, and cross-conversion matching flows.
- **My Level**: **L4 - Advanced**
- **Evidence of capability**:
  - can navigate orchestration flow in `matching/core/matching.py`
  - can modify execution order/parallel behavior based on runtime constraints
  - can investigate matching failures using markers, logs, and intermediate states

### 6. Result Generation and Publishing

- **Functionality**: save result artifacts and publish records via Pub/Sub.
- **My Level**: **L3 - Proficient**
- **Evidence of capability**:
  - can support batched publishing flow and fallback handling
  - can troubleshoot payload/format and publish-count mismatches
  - can maintain result generation paths for downstream systems

### 7. Performance and Parallel Processing

- **Functionality**: optimize CPU usage, process pools, and memory-aware execution.
- **My Level**: **L4 - Advanced**
- **Evidence of capability**:
  - can tune core allocation and parallel matching settings
  - can reason about lock-based coordination and multi-process bottlenecks
  - can stabilize high-volume runs through practical performance tuning

### 8. Reliability, Logging, and Operability

- **Functionality**: maintain production readiness through observability and safe failure behavior.
- **My Level**: **L4 - Advanced**
- **Evidence of capability**:
  - can trace failures end-to-end with logs, markers, and status events
  - can identify common operational issues in scheduled batch runs
  - can support reruns and production debugging with low turnaround time

## Skill Summary

- **Current profile**: strong production contributor with advanced capability in orchestration, feature processing, and performance/reliability.
- **Most mature areas**: configuration-driven execution, matching orchestration, performance tuning, operational debugging.
- **Good working areas with growth potential**: DB contract hardening and publish reliability patterns.

