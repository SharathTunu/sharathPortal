# DNStar Functionalities and Required Skills

## Project overview

DNStar is a high-performance, GPU-accelerated video analytics platform built on NVIDIA DeepStream, TensorRT, CUDA, and GStreamer. It processes RTSP streams and video files, runs deep learning inference, tracks objects, computes spatial analytics, and emits metadata for downstream systems.

At a high level, the system combines:

- A core inference pipeline (`DNStar` shared library and `DNStarProd` executable).
- A manager process that monitors and orchestrates batch/realtime workloads.
- Custom DeepStream plugins for analytics and tracking.
- Optional Python bindings for programmatic integration.

## Core functionalities implemented in this codebase

## 1) Multi-source video ingestion and pipeline execution

- Reads one or more sources from config files (RTSP and file URIs).
- Builds optimized or visualized processing pipelines.
- Supports configurable muxing, batching, queueing, drop-frame behavior, and streaming output.

## 2) Deep learning inference on GPU

- Runs object detection using TensorRT-compatible models.
- Supports multiple model types (person, head, car, person+head, and related variants).
- Uses custom inference parsers/plugins and model-specific configuration files.

## 3) Object tracking

- Integrates with DeepStream tracker interface.
- Supports multiple tracker modes, including a custom BYTETrack-based low-level tracker (`DSTracker`).
- Exposes tracker tuning parameters such as confidence thresholds and matching settings.

## 4) Scene analytics and event generation

- Performs line crossing and polygon analytics through a custom plugin (`DSAnalytics`).
- Supports occupancy, queue, checkout, and event-style zones (for example: tripwire, danger zone, overtime).
- Uses ROI config files to define camera-specific geometry and behavior.

## 5) Metadata generation and publishing

- Produces analytics metadata in configurable output formats (disk JSON, publisher, or both).
- Supports publisher-oriented integration through topic/project config files.
- Can generate periodic metadata or end-of-stream metadata depending on runtime settings.

## 6) Orchestration, monitoring, and fault handling

- Includes manager-level logic to poll source/config directories and run pipeline jobs.
- Uses marker files to represent source lifecycle states (start, processing, end, error).
- Implements restart thresholds, GPU utilization monitoring, and timeout-based recovery policies.

## 7) Operational outputs and observability

- Emits structured logs and processing metadata.
- Optionally saves output video and cropped objects.
- Provides configurable logging levels and performance tuning knobs.

## 8) Build, packaging, and test support

- CMake-based build for C++/CUDA modules and plugins.
- Docker-based execution workflows for dGPU and Jetson environments.
- Includes unit test targets and test configuration files.

## 9) Python extensibility

- Exposes Python bindings via `pybind11` for integration with Python workflows.
- Includes supporting Python utilities (for example, group tracking and helper scripts).

## Skills required to build a system like this

## A) Core software engineering skills

- Advanced C++ (C++17): performance-sensitive code, memory ownership, modular architecture.
- Build systems: CMake for multi-module native builds and external dependency wiring.
- Linux development and debugging: process management, logging, profiling, runtime tuning.

## B) Video and streaming systems expertise

- GStreamer pipeline design: elements, pads, buffering, muxing, and sink behavior.
- DeepStream SDK integration: plugin contracts, metadata flow, and batched frame processing.
- RTSP and media transport fundamentals for reliable realtime ingestion.

## C) GPU and inference engineering

- CUDA basics and GPU memory/performance considerations.
- TensorRT model deployment, engine compatibility, and optimization trade-offs.
- Practical computer vision deployment knowledge (pre/post-processing, confidence tuning, NMS behavior).

## D) Tracking and analytics algorithm knowledge

- Multi-object tracking concepts (association, confidence thresholds, lost track handling).
- Spatial analytics design (line crossing directionality, polygon occupancy semantics).
- Event logic and temporal constraints (dwell time, restricted windows, thresholding).

## E) Data integration and platform skills

- Metadata schema design and message publishing patterns.
- Config-driven architecture and environment-specific deployment practices.
- Cloud/event pipeline integration experience (topic/project routing and reliability patterns).

## F) MLOps and operations skills

- Containerization with Docker for reproducible runtime environments.
- GPU-aware deployment operations (driver/toolkit/runtime compatibility).
- Profiling and production diagnostics (GPU utilization, memory tools, stress testing).

## G) Testing and quality skills

- Unit and integration testing for analytics correctness and pipeline behavior.
- Performance and load testing for multi-stream workloads.
- Regression validation for model/tracker/config changes.

