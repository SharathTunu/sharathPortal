# Sharath Tunuguntla — Q&A Knowledge Base for RAG Bot
# Format: Each Q&A is a self-contained chunk for retrieval.
# Questions cover identity, skills, projects, tools, and experience.

---

Q: Who are you?
A: I am Sharath Tunuguntla, an Applied ML Engineer with 6+ years of experience building, training, and deploying computer vision and AI systems in real-world production environments. I specialise in object detection, Re-Identification (ReID), multi-object tracking, GPU-accelerated inference, and MLOps infrastructure.

---

Q: What is your professional background?
A: I am an Applied ML Engineer with over 6 years of hands-on experience. My work spans the full pipeline from training deep learning models to deploying and maintaining them in production across hundreds of remote servers. I have built systems for retail analytics, airport operations, warehouse automation, and traffic monitoring.

---

Q: What are your strongest skills?
A: My strongest skills are Model Training and Computer Vision (level 5 out of 5) and MLOps and Deployment at Scale (level 5 out of 5). I am also highly skilled in ReID and Multi-Camera Tracking, Real-Time Video Analytics, Python Systems Engineering, and C++ development, all rated level 4 out of 5.

---

Q: What programming languages do you know?
A: I primarily use Python (level 5 out of 5) and C++ (level 4 out of 5). I also have experience with JavaScript, HTML, CSS, and Shell scripting.

---

Q: What ML frameworks and tools do you use?
A: I am proficient in PyTorch, TensorFlow, ONNX, TensorRT, NVIDIA DeepStream, and OpenCV. For YOLO-based models I have worked with YOLOv4, YOLOX, and YOLOv11. I also use FFmpeg for video processing and GStreamer for pipeline design.

---

Q: What is your experience with Python?
A: Python is my primary language and I am rated level 5 out of 5. I use it for ML model development, production services, schedulers, watchdog loops, REST APIs, multiprocessing pipelines, data processing with pandas and NumPy, and web backends with Django and Flask.

---

Q: What is your experience with C++?
A: I am rated level 4 out of 5 in C++. I use it for production-grade computer vision systems, DeepStream plugins, GStreamer pipelines, and native build systems using CMake. I am comfortable with C++17 and performance-sensitive code.

---

Q: What AI and ML models have you trained?
A: I have trained more than 10 deep learning models including: SigLIP for ReID feature extraction (80% accuracy), YOLOv11s for pallet detection (98% accuracy), multi-class YOLOx for person and bag detection (90% accuracy), YOLO-based car detection (96% accuracy), YOLO-based person detection (98% accuracy), YOLOx color classification for employee monitoring (90% accuracy), YOLOv4 for traffic counting (95–98% accuracy), YOLOX for aircraft engine-on detection (85% accuracy), multi-class U-Net segmentation (95% accuracy), and multi-class YOLACT++ segmentation (95% accuracy).

---

Q: What object detection models have you worked with?
A: I have trained and deployed YOLOv4, YOLOX, YOLOv11s, and YOLACT++ for various detection tasks including person detection, vehicle detection, bag detection, pallet detection, and aircraft engine state detection. Accuracies range from 85% to 98% depending on the task.

---

Q: Have you worked on image segmentation?
A: Yes. I have trained a multi-class U-Net segmentation model on vehicle telemetry data using the cityscapes dataset achieving 95% accuracy, and a multi-class YOLACT++ segmentation model for detecting below-the-wing vehicles at airports with 95% accuracy.

---

Q: What is your experience with Re-Identification (ReID)?
A: ReID is one of my core specialisations. I trained a SigLIP model to extract feature vectors for person ReID across multiple cameras, achieving 80% accuracy. I built a production ReID pipeline combining ViT and SigLIP2 embeddings with sparse Hungarian matching, multi-model similarity fusion, embedding caching, and multi-GPU extraction. I also built a Streamlit-based ReID QA tool and integrated vLLM to reduce QA review time from ~50 man-hours to 10–15 hours.

---

Q: What is your experience with object tracking?
A: I have implemented Kalman filter-based tracking across multiple projects including person tracking, vehicle tracking, bag tracking, and car tracking, with approximately 5% tracking loss in most deployments. I also work with BYTETrack-based tracking through the DNStar platform (DSTracker) and have built Hungarian matching pipelines for person assignment at scale.

---

Q: What algorithms have you built beyond model training?
A: I have built a Break Check algorithm using YOLOv4, tracking, and Mean-Shift clustering (80% accuracy), a Pose Estimation algorithm using a skeleton model to count object touches (85% accuracy), a Checkout Summary algorithm for customer checkout times (98% accuracy), a ResNet-based employee-customer interaction classifier (95% accuracy), a loan offer filtering algorithm, a Deep Q-learning reinforcement learning agent for 2D grid navigation, and an Automatic Speech Recognition system using RNN, DNN, and CNN architectures.

---

Q: What is your experience with LLMs and Generative AI?
A: I am rated level 3 out of 5 in LLM and GenAI integration, and it is a growing area. I have integrated vLLM into the ReID QA pipeline to automate review, created a RAG chatbot on my resume to build a portfolio chatbot, used Qwen VL (Qwen3-VL-8B-Instruct) for vision-language QA workflows, used Gemini Vision API for ReID verification with retries and parallel workers, and built TensorRT engine workflows for model deployment.

---

Q: Have you built a RAG chatbot?
A: Yes. I created a RAG chatbot based on my resume and built a portfolio chatbot that can answer questions about my background and experience. This chatbot is available on my portfolio portal.

---

Q: What is your MLOps experience?
A: MLOps is one of my strongest areas (level 5 out of 5). I built a native automated deployment and management service that maintains, upgrades, and rolls back software across 400+ remote servers in US and EU regions. I led the conversion of an entire ML platform into a microservices architecture using Docker. I built a GPU availability manager for dynamic algorithm scheduling, integrated etcd for distributed config management, used RabbitMQ for message brokering, and set up CI/CD pipelines with Jenkins and Celery.

---

Q: How many servers have you managed deployments across?
A: I built and maintain a deployment system that manages software across 400+ remote servers across US and EU regions, supporting automated upgrades, rollbacks, and health monitoring without manual intervention.

---

Q: What is your Docker experience?
A: I have extensive Docker experience. I led the conversion of an entire ML platform into a microservices architecture with Docker images for every service. I manage images on Docker Hub, use the Docker SDK in Python, write Docker Compose files for analytics workloads, and have deployed containerised services on AWS. My Docker skill is rated level 3 to 4 out of 5 depending on the project context.

---

Q: What cloud platforms have you worked with?
A: I have deployed web applications and services on AWS using containerised Docker services with Celery and Jenkins for CI/CD. I have also used Google Cloud Pub/Sub for alerting and metadata publishing in the camera recorder and ReID pipelines.

---

Q: What is your experience with real-time video analytics?
A: I am rated level 4 out of 5 in real-time video analytics. I built a near real-time analytics platform processing 80 simultaneous camera streams on dGPU hardware with a 60-second latency target. I have built live streaming inference pipelines, traffic heat map generators, foot and vehicle traffic counters, abandoned baggage detection systems, parking and overtime alert systems, and an aircraft engine-on detector, all running in production.

---

Q: What is the DNStar platform?
A: DNStar is a GPU-accelerated video analytics platform I have worked on, built on NVIDIA DeepStream, TensorRT, CUDA, and GStreamer. It handles multi-source RTSP and file video ingestion, deep learning inference, object tracking with a custom BYTETrack-based tracker (DSTracker), scene analytics including line crossing and polygon occupancy, metadata generation and publishing, and manager-level orchestration with GPU health monitoring.

---

Q: What are your skill levels on DNStar?
A: On DNStar I am rated (scale 1–5): C++17 development 4, CMake and build systems 4, GStreamer pipeline design 4, NVIDIA DeepStream integration 4, Linux development and debugging 4, configuration-driven architecture 5, object tracking workflows 4, spatial analytics (ROI/line/polygon) 5, metadata generation and integration 4, Docker-based deployment 3, CUDA programming 1, TensorRT internals 1.

---

Q: What is the Appmanager service?
A: Appmanager is a Python-based service control and deployment manager I built. It provides a root-only CLI for registering and unregistering services, a keepalive loop that enforces run windows and manages service lifecycle via shell scripts, matching pipeline gating with Docker and DNStar checks, deployment automation that polls Command Center APIs and handles Docker image downloads and install/rollback, and self-supervision to ensure its own processes stay running.

---

Q: What are your skill levels on Appmanager?
A: On Appmanager I am rated (scale 1–5): CLI and registration 4, keepalive and scheduling 5, matching gating and YAML 5, deployments and REST 4, logging and observability 4, Linux/systemd packaging 4.

---

Q: What is the Manager orchestration service?
A: Manager is a Python orchestration service for GPU-based video analytics. It supervises core polling and scheduling services with automatic restart, monitors GPU health (utilisation, memory, temperature, thermal throttling) for placement decisions, interprets camera configs to determine processing mode and run windows, generates Docker Compose files for each workload, and controls analytics container start/stop based on resource availability and scheduling rules. Its tech stack includes Python, pandas, NumPy, OpenCV, Docker SDK, and NVIDIA GPU tools.

---

Q: What is the camera recorder service?
A: The camera recorder is a service I built and maintain that manages per-camera RTSP video recording using FFmpeg. It handles launcher scripts for each camera, FFmpeg command generation from templates (supporting unencrypted, segmented, and encrypted modes), timezone-aware scheduling, AES-CBC stream URL encryption, Verkada JWT token management with retry and backoff, deep video diagnostics using ffprobe, a GPU-parallel re-encode and repair pipeline using ThreadPoolExecutor, and FPS anomaly alerting via Google Pub/Sub.

---

Q: What are your skill levels on the camera recorder?
A: On the camera recorder I am rated (scale 1–5): Python services 5, FFmpeg and video processing 4, Cloud (GCP) and Pub/Sub networking 4, security and cryptography 4, containers and Linux ops 5.

---

Q: What is the matching pipeline?
A: The matching pipeline is a system I work on that correlates ReID features across zones to produce person journey records. It uses config-driven execution via matching.yml, validates inputs and manages job lifecycle, maps zones from CSV databases, loads and normalises .npy feature files, orchestrates property, dwell, and cross-conversion matching flows, generates results and publishes them via Pub/Sub, and uses parallel processing with multiprocessing for performance.

---

Q: What are your skill levels on the matching pipeline?
A: On the matching pipeline I am rated (scale 1–5): configuration-driven execution 4, input validation and job lifecycle 4, DB CSV ingestion and zone mapping 4, feature loading and preprocessing 4, matching orchestration 4, result generation and publishing 4, performance and parallel processing 4, reliability, logging, and operability 4.

---

Q: What is the real-time matching pipeline?
A: The real-time entry-exit matching pipeline is a production system I built for person ReID that pairs people seen entering and exiting zones across cameras. It uses sparse Hungarian matching, ViT and SigLIP2 embeddings with multi-model fusion, an embedding cache for efficiency, multi-GPU parallel extraction, memory optimisation to handle OOM risks, pub-sub integration for downstream data, and Gemini Vision API for result verification.

---

Q: What are your skill levels on the real-time matching pipeline?
A: On the real-time matching pipeline I am rated (scale 1–5): core person pairing and assignment 5, embedding extraction (ViT/OML) 4, SigLIP2 integration 4, multi-model similarity fusion 4, embedding cache design 4, scalability and multi-GPU execution 4, memory and runtime optimisation 5, data publishing and pub-sub integration 4, productionisation and deployment support 4, verification with Gemini Vision 4, analysis and visualisation tooling 4, data quality filtering with YOLO 4.

---

Q: What is your web development experience?
A: I am rated level 4 out of 5 in web development. I have built backend web applications using Flask and Django with MVC architecture, set up REST API frameworks, refactored large-scale codebases, deployed apps on AWS with Celery and Jenkins, built frontend interfaces using JavaScript, HTML, CSS, and Jinja, configured nginx as a reverse proxy, and built internal tools including a Ground Truth QA web tool and a remote terminal access web service using Flask and Ansible.

---

Q: What personal projects have you built?
A: I built a full-stack Django web application called My Dairy, which includes a Budget Planner that tracks income and expenditures and generates a weekly Excel export, and a Resume Builder that generates auto-formatted resumes from templates so users can download them without worrying about fonts or alignment. I also built a RAG-based portfolio chatbot trained on my resume.

---

Q: What is your experience with GStreamer?
A: I am rated level 4 out of 5 in GStreamer pipeline design. I use GStreamer as the foundation for the DNStar video analytics platform, designing pipeline composition, element behaviour, buffering, muxing, and sink configurations for RTSP and file-based video sources.

---

Q: What is your experience with NVIDIA DeepStream?
A: I am rated level 4 out of 5 in NVIDIA DeepStream integration. I use DeepStream for building GPU-accelerated inference and tracking pipelines, integrating custom analytics plugins, managing batched frame processing, and handling metadata flow across the pipeline. I have used it for traffic heat maps, foot counting, vehicle counting, and other real-time analytics workloads.

---

Q: What is your experience with TensorRT?
A: I use TensorRT through DeepStream and ONNX-based workflows for model deployment and inference optimisation. However, I have limited experience with TensorRT internals and kernel-level optimisation, which I rate level 1 out of 5. My practical deployment usage through tooling is stronger.

---

Q: What is your experience with CUDA?
A: My CUDA experience is limited (level 1 out of 5). I use CUDA through higher-level tools like DeepStream and TensorRT but do not write custom CUDA kernels. This is an area I am aware of but have not worked on at a low level.

---

Q: What is your experience with Ansible?
A: I have used Ansible to build a native remote terminal access service that allows support teams to perform manual tasks on all remote servers across regions without direct server access. I use it as part of the broader MLOps automation stack alongside Flask and shell scripting.

---

Q: What is your experience with Streamlit?
A: I built a full Streamlit-based ReID QA tool with paginated image grids, session state management, multi-column layouts, callback and form workflows, dwell-time calculation, CSV export, and save/load session state for long-running QA sessions. I am rated level 4 out of 5 in Streamlit.

---

Q: What video processing tools do you use?
A: I regularly use FFmpeg for video recording, segmentation, encryption, and re-encoding. I use ffprobe for deep video diagnostics including codec analysis, frame error scanning, PTS/DTS checks, keyframe inspection, and variable frame rate detection. I also use OpenCV for image processing, DeepStream for GPU-accelerated video analytics pipelines, and GStreamer for pipeline composition.

---

Q: What is your experience with spatial analytics and ROI configuration?
A: I am rated level 5 out of 5 in spatial analytics including ROI design, line crossing, polygon occupancy, event logic, and analytics behaviour tuning. I have strong ownership of rule configuration and analytics behaviour on the DNStar platform, covering zones for occupancy, queue, checkout, danger zone, and overtime detection.

---

Q: What databases and data tools have you worked with?
A: I have worked with PostgreSQL and SQL for relational data management, pandas and NumPy for tabular data processing and analytics, etcd for distributed configuration management, and RabbitMQ for message brokering. I also work extensively with JSON, YAML, and CSV-based configuration and data formats.

---

Q: What is your experience with message queuing and pub/sub systems?
A: I have integrated RabbitMQ for message brokering within the ML platform, and Google Cloud Pub/Sub for publishing ReID results, camera FPS alerts, and analytics metadata in the camera recorder and matching pipelines.

---

Q: What is your overall skill rating summary?
A: My overall skill ratings on a scale of 1 to 5 are: Model Training and Computer Vision 5, MLOps and Deployment at Scale 5, ReID and Multi-Camera Tracking 4, Real-Time Video Analytics 4, Python Systems Engineering 4, C++ and Native Development 4, Web Development with Django and Flask 4, LLM and GenAI Integration 3, CUDA and TensorRT Internals 1.

---

Q: What industries have you worked in?
A: I have built AI systems for retail (customer interaction monitoring, checkout analysis, break compliance), airports (aircraft engine-on detection, below-the-wing vehicle tracking), warehouses (pallet detection), traffic and smart city (foot and vehicle counting, heat maps), and financial services (loan offer filtering algorithm).

---

Q: What is your most impactful achievement?
A: One of my most impactful achievements is building an automated deployment and management service that maintains software across 400+ remote servers in the US and EU, with zero-downtime upgrades and rollback. Another major achievement is integrating vLLM into the ReID QA pipeline, reducing manual review effort from approximately 50 man-hours to 10–15 hours per cycle.

---

Q: Can you work on both research and production?
A: Yes. I bridge research-style modelling work with practical production deployment. I can train and evaluate models, design algorithms, optimise pipelines for performance and scale, and deploy and maintain them in production across large server fleets. My profile is strongest on the applied and production side.

---

Q: What are your weakest areas or areas you are still growing in?
A: My weakest areas are CUDA programming (level 1 out of 5) and TensorRT internals (level 1 out of 5), where I use these technologies through higher-level tools rather than at the kernel level. LLM and GenAI integration is rated level 3 out of 5 and is an area I am actively developing through projects like vLLM integration, RAG chatbots, and vision-language model usage.

---

Q: How can I contact Sharath or learn more?
A: You can explore Sharath's work through this portfolio. For deeper conversations about collaboration, opportunities, or project enquiries, reaching out directly is encouraged. The portfolio chatbot can answer specific questions about background, skills, and projects.