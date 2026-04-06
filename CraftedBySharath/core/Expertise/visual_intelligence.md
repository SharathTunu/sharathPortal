# Visual Intelligence Achievements

## Real-Time Video Analytics

- Developed a near real-time analytics platform (60-second delay) processing data from **80 simultaneous camera streams** on previous-gen dGPU hardware.
- Built real-time live streaming pipelines for computer vision inference at scale.
- Built an inference pipeline for **helpdesk kiosk cameras** that tracks interaction times and passerby flow counts.
- Maintained video recording infrastructure using **FFmpeg** for all algorithm pipelines.

## People & Object Tracking

- Developed **Re-Identification (ReID)** across cameras using SigLIP-derived feature vectors with **80% accuracy**.
- Implemented **Kalman filter-based tracking** across multiple projects — achieving ~5% tracking loss for people, vehicles, bags, and cars.
- Built an **Abandoned Baggage Detection system** in C++ and Python (ONNX) that:
  - Detects stationary bags without nearby persons using YOLOx
  - Applies **2D-to-3D coordinate conversion** to calculate real-world bag-to-camera distance
- Built a **Parking & Overtime Alert system** that tracks cars in parking lots and triggers alerts when a spot is occupied beyond its time limit.

## Traffic & Flow Analysis

- Built a **traffic flow heat map generator** using DeepStream and OpenCV that tracks people across camera views throughout the day and renders a heat gradient visualization of movement patterns.
- Developed **foot and vehicle traffic counting** algorithms using YOLOv4 detection and Kalman filter tracking with **95–98% accuracy**.

## Behavioral & Interaction Analysis

- Developed an **Employee Interaction Algorithm** using YOLOx uniform-color classification to identify employees and track their interactions with machinery.
- Built a **classification system** measuring average employee–customer interaction durations using a ResNet-based model with **~95% accuracy**.
- Developed a **Pose Estimation algorithm** using a skeleton model to detect and count physical contact with objects (**85% accuracy**).
- Built a **Break Check algorithm** using detection, tracking, and Mean-Shift clustering to verify break compliance (**80% accuracy**).

## Specialized Detection

- Trained and deployed an **aircraft engine-on detection algorithm** (YOLOX) to determine if an engine is running while the aircraft is at a gate (**85% accuracy**).
- Trained a **wooden pallet detection model** (YOLOv11s) for warehouse environments (**98% accuracy**).
- Built a **checkout analysis system** computing average customer checkout times with **98% accuracy**.

## Tools & Frameworks

- **DeepStream, TensorRT, ONNX, OpenCV, FFmpeg, nvinfer, nvtracker**.
- **YOLOv4, YOLOX, YOLOv11, SigLIP, ResNet, Skeleton/Pose models**.
- **C++, Python** for real-time inference and stream processing.
