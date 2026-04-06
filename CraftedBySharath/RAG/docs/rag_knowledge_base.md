# Sharath Tunuguntla — Professional Knowledge Base
# Optimised for RAG retrieval. Each section is self-contained and factual.
#
# SKILL RATING SCALE (used consistently throughout this document):
# 1 — Beginner: basic awareness, needs guidance
# 2 — Familiar: can contribute with some support
# 3 — Proficient: independent ownership of routine tasks and features
# 4 — Advanced: designs solutions, handles edge cases, reviews others
# 5 — Expert: defines architecture, go-to authority, mentors others

---

## WHO I AM

My name is Sharath Tunuguntla. I am an Applied ML Engineer with 6+ years of experience building, training, and deploying computer vision and AI systems in real-world production environments. I specialise in object detection, Re-Identification (ReID), multi-object tracking, GPU-accelerated inference, and MLOps infrastructure.

---

## SUMMARY OF SKILLS

- Computer Vision: object detection, segmentation, classification, ReID, tracking, pose estimation
- ML Frameworks: PyTorch, TensorFlow, ONNX, TensorRT, DeepStream, OpenCV
- YOLO models: YOLOv4, YOLOX, YOLOv11
- Languages: Python (skill level 5), C++ (skill level 4)
- MLOps: Docker, Ansible, Jenkins, Celery, REST APIs, AWS, RabbitMQ, etcd
- Web: Django, Flask, JavaScript, HTML, CSS, nginx, PostgreSQL
- LLM/GenAI: RAG, vLLM, Qwen VL, Gemini Vision API

---

## AI / ML MODELS TRAINED

- SigLIP model for Re-Identification (ReID) feature extraction across cameras — 80% accuracy
- YOLOv11s for wooden pallet detection in warehouses — 98% accuracy
- Multi-class YOLOx for person and bag detection (abandoned baggage) — 90% accuracy, ~5% tracking loss
- YOLO-based car detection for parking and overtime alerts — 96% accuracy, ~5% tracking loss
- YOLO-based person detection for traffic flow heat maps — 98% accuracy
- Multi-class YOLOx color classification for employee interaction monitoring — 90% accuracy
- YOLOv4 detection with Kalman filter for foot and vehicle traffic counting — 95–98% accuracy
- YOLOX model for aircraft engine-on detection at airport gates — 85% accuracy
- Multi-class U-Net segmentation on vehicle telemetry using cityscapes dataset — 95% accuracy
- Multi-class YOLACT++ segmentation for below-the-wing airport vehicles — 95% accuracy

---

## AI / ML ALGORITHMS BUILT

- Break Check algorithm using YOLOv4, tracking, and Mean-Shift clustering — 80% accuracy
- Pose Estimation algorithm using skeleton model to count object touches — 85% accuracy
- Checkout Summary algorithm for average customer checkout times — 98% accuracy
- ResNet-based classification for employee–customer interaction time measurement — 95% accuracy
- Filtering algorithm for loan offer generation based on user parameters and historical data
- Neural Network Reinforcement Learning agent (Deep Q-learning) for 2D grid navigation
- Automatic Speech Recognition system using RNN, DNN, CNN with TensorFlow and Caffe

---

## LLM AND GENAI WORK

- Integrated vLLM into the ReID QA pipeline, reducing human review from ~50 man-hours to 10–15 hours
- Created a RAG chatbot on my resume to build a portfolio chatbot
- Used Qwen VL (Qwen3-VL-8B-Instruct) for vision-language workflows in QA tooling
- Used Gemini Vision API for verification of ReID matching results
- Built TensorRT engine workflows using trtexec for model deployment

---

## MLOPS AND DEPLOYMENT

- Built a native automated deployment and management service managing software across 400+ remote servers in US and EU regions, with upgrade and rollback support
- Built a native remote terminal access service using Ansible and Flask for support teams to operate across all remote servers without direct access
- Led conversion of an entire ML platform into a microservices architecture with Docker images for every service
- Managed Docker-based deployments and images on Docker Hub
- Used Docker, Celery, and Jenkins for CI/CD and background task management
- Deployed web applications on AWS using containerised services
- Built a GPU availability manager to schedule and route algorithm processing based on live GPU capacity
- Built a Ground Truth QA tool for QA teams to analyse production algorithm outputs across client sites
- Integrated etcd for distributed configuration management and RabbitMQ for message brokering
- Developed REST APIs and REST clients to sync state changes to production servers
- Set up REST API frameworks using Django for backend data management
- Tech stack: Docker, Docker Hub, Ansible, Flask, Jenkins, Celery, AWS, RabbitMQ, etcd, nginx, Ubuntu, RHEL, Shell scripting, Git, REST, SQL, PostgreSQL, Python, C++

---

## REAL-TIME VIDEO ANALYTICS

- Built a near real-time analytics platform with 60-second delay processing 80 simultaneous camera streams on dGPU hardware
- Built real-time live streaming pipelines for computer vision inference at scale
- Built an inference pipeline for helpdesk kiosk cameras tracking interaction times and passerby counts
- Maintained video recording infrastructure using FFmpeg for all algorithm pipelines
- Built a traffic flow heat map generator using DeepStream and OpenCV tracking people across camera views
- Developed foot and vehicle traffic counting with YOLOv4 and Kalman filter — 95–98% accuracy
- Built an Abandoned Baggage Detection system in C++ and Python (ONNX) using YOLOx with 2D-to-3D coordinate conversion for real-world bag-to-camera distance calculation
- Built a Parking and Overtime Alert system tracking cars and triggering alerts when spots exceed time limits
- Built an aircraft engine-on detection algorithm using YOLOX — 85% accuracy
- Built a checkout analysis system for average customer checkout times — 98% accuracy
- Tools: DeepStream, TensorRT, ONNX, OpenCV, FFmpeg, nvinfer, nvtracker, YOLOv4, YOLOX, YOLOv11, SigLIP, ResNet, Skeleton/Pose models, C++, Python

---

## RE-IDENTIFICATION (REID) SYSTEM

- Developed ReID across cameras using SigLIP-derived feature vectors — 80% accuracy
- Built a production ReID pipeline combining ViT and SigLIP2 embeddings with sparse Hungarian matching
- Implemented multi-model similarity fusion strategies: weighted, max, min
- Added embedding cache to reduce repeated extraction cost
- Implemented parallel extraction with multi-GPU support
- Addressed OOM risks, improved matrix handling, and optimised assignment for high-volume inputs
- Added pub-sub integration for downstream data flow
- Built productionised Docker setup with runtime controls (zone/date filtering)
- Used Gemini Vision API for verification with resume, retries, and parallel worker patterns
- Integrated vLLM to automate QA review, reducing effort from ~50 man-hours to 10–15 hours
- Built a Streamlit-based ReID QA tool with paginated image grids, session state, CSV export, and dwell-time calculation

---

## DNSTAR VIDEO ANALYTICS PLATFORM

DNStar is a GPU-accelerated video analytics platform built on NVIDIA DeepStream, TensorRT, CUDA, and GStreamer.

What it does:
- Multi-source RTSP and file video ingestion
- Deep learning inference using TensorRT-compatible models (person, head, car, person+head)
- Object tracking using custom BYTETrack-based tracker (DSTracker)
- Scene analytics: line crossing, polygon occupancy, queue, checkout, danger zone, overtime
- Metadata generation and publishing (disk JSON or pub/sub)
- Manager-level orchestration with marker files for source lifecycle states
- GPU utilisation monitoring and timeout-based recovery
- Python bindings via pybind11

My skill levels on DNStar (scale 1–5):
- C++17 development: 4
- CMake and build systems: 4
- GStreamer pipeline design: 4
- NVIDIA DeepStream integration: 4
- Linux development and debugging: 4
- Configuration-driven architecture: 5
- Object tracking workflows: 4
- Spatial analytics (ROI/line/polygon): 5
- Metadata generation and integration: 4
- Docker-based deployment: 3
- CUDA programming: 1
- TensorRT internals: 1

---

## MANAGER ORCHESTRATION SERVICE

Manager is a Python orchestration service for GPU-based video analytics.

What it does:
- Supervises core polling and scheduling services with automatic restart
- Monitors GPU health (utilisation, memory, temperature, thermal throttling) for placement decisions
- Interprets camera configs to decide processing mode and run windows
- Generates source/ROI artifacts and per-workload Docker Compose files
- Starts/stops analytics workloads based on resource availability and scheduling rules
- Controls DeepSense lifecycle using backlog and time-window policies

Tech stack: Python, pandas/NumPy, OpenCV, Docker SDK, Linux process/file operations, NVIDIA GPUs, Docker/Compose

---

## APPMANAGER SERVICE

Appmanager is a Python-based service control and deployment manager.

What it does:
- CLI for registering/unregistering services (root-only)
- Keepalive loop: enforces run windows, starts/stops services via shell scripts, cleans up logs and metadata
- Matching pipeline gating: Docker checks, recording windows, DNStar markers, ReID image backlog
- Deployment automation: polls Command Center APIs, downloads Docker images from GHCR, runs install/rollback
- Self-supervision: ensures deployments and keepalive processes stay running via PID and log freshness checks

My skill levels on Appmanager (scale 1–5):
- CLI and registration: 4
- Keepalive and scheduling: 5
- Matching gating and YAML: 5
- Deployments and REST: 4
- Logging and observability: 4
- Linux/systemd packaging: 4

---

## CAMERA RECORDER SERVICE

The camera recorder manages per-camera RTSP recording using FFmpeg.

What it does:
- Per-camera launcher scripts with start/stop orchestration
- FFmpeg command construction from templates (unencrypted, segmented, encrypted)
- Camera model with timezone, schedule, and capture interval
- Calendar/Command Center hours integration
- Recording modes: unencrypted, encrypted, re-encode
- Stream URL encryption using AES-CBC
- Verkada JWT token flow with retry and backoff
- Deep video diagnostics using ffprobe
- Re-encode and repair pipeline with GPU parallelism using ThreadPoolExecutor
- Google Pub/Sub alerting for FPS anomalies

My skill levels on the camera recorder (scale 1–5):
- Python services: 5
- FFmpeg and video processing: 4
- Cloud (GCP) and Pub/Sub networking: 4
- Security and cryptography: 4
- Containers and Linux ops: 5

---

## MATCHING PIPELINE

The matching pipeline correlates ReID features across zones to produce person journey records.

What it does:
- Config-driven execution via matching.yml
- Input validation, job lifecycle management (start/finish/error)
- Zone mapping from CSV databases (property, dwell, cross-conversion zones)
- Feature loading: reads/filters/normalises .npy feature files with PMR metadata alignment
- Orchestrates property, dwell, and cross-conversion matching flows
- Result generation and Pub/Sub publishing
- Parallel processing with CPU core allocation and multiprocessing

My skill levels on the matching pipeline (scale 1–5):
- Configuration-driven execution: 4
- Input validation and job lifecycle: 4
- DB CSV ingestion and zone mapping: 4
- Feature loading and preprocessing: 4
- Matching orchestration: 4
- Result generation and publishing: 4
- Performance and parallel processing: 4
- Reliability, logging, and operability: 4

---

## REAL-TIME MATCHING (RT-ENTRY-MATCHING)

Real-time entry-exit matching pipeline for person ReID.

My skill levels (scale 1–5):
- Core person pairing and assignment pipeline: 5
- Embedding extraction (ViT / OML): 4
- SigLIP2 integration for ReID: 4
- Multi-model similarity fusion: 4
- Embedding cache design and reuse: 4
- Scalability and multi-GPU execution: 4
- Memory and runtime optimisation: 5
- Data publishing and pub-sub integration: 4
- Productionisation and deployment support: 4
- Verification workflow using Gemini Vision: 4
- Analysis and visualisation tooling: 4
- Data quality filtering with YOLO: 4

---

## WEB DEVELOPMENT

- Built backend web applications using Flask and Django with MVC architecture
- Set up REST API frameworks using Django
- Refactored large-scale Django/Flask codebases to reduce duplication
- Deployed web apps on AWS with Celery for async tasks and Jenkins for CI/CD
- Built frontend interfaces using JavaScript, HTML, CSS, and Jinja templating
- Configured and maintained nginx as a reverse proxy
- Built a Ground Truth QA web tool for production algorithm analysis
- Built a remote terminal access web service using Flask and Ansible

Personal projects:
- My Dairy: full-stack Django web app with Budget Planner (weekly Excel export) and Resume Builder (template-driven, auto-formatted PDF download)

Tech stack: Python, Django, JavaScript, HTML, CSS, Jinja, nginx, Flask, REST, PostgreSQL, SQL, AWS, Docker, Postman, Jupyter Notebook

---

## OVERALL SKILL RATINGS (scale 1–5)

- Model Training and Computer Vision: 5
- MLOps and Deployment at Scale: 5
- ReID and Multi-Camera Tracking: 4
- Real-Time Video Analytics: 4
- Python Systems Engineering: 4
- C++ and Native Development: 4
- Web Development (Django/Flask): 4
- LLM and GenAI Integration: 3
- CUDA and TensorRT Internals: 1