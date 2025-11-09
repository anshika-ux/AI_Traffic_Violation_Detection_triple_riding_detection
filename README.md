# 🏍️ Triple Riding Detection System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8-green.svg)](https://github.com/ultralytics/ultralytics)
[![MongoDB](https://img.shields.io/badge/MongoDB-4.4%2B-green.svg)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

An advanced computer vision system designed to automatically detect and report triple riding violations on motorcycles. Built on YOLOv8's state-of-the-art object detection capabilities, this system provides real-time monitoring and automated violation reporting for traffic safety enforcement.

## 🎯 Key Features

- **High-Precision Detection**
  - YOLOv8-powered object detection for accurate rider and vehicle identification
  - Smart rider-vehicle association using IoU and distance metrics
  - Configurable confidence thresholds for optimal detection accuracy

- **Comprehensive Violation Monitoring**
  - Automatic detection of triple riding violations
  - Visual indicators with red boxes for violations
  - Confidence scoring for reliable violation reporting

- **Robust Data Management**
  - MongoDB integration for persistent violation records
  - Detailed CSV reports with violation statistics
  - Automated image and video frame analysis

- **Advanced Visualization**
  - Clear violation markers with customizable indicators
  - Confidence score display options
  - Direction arrows for enhanced visualization
  - Compact violation view mode

## �️ System Requirements

### Core Requirements
- **Python**: Version 3.8 or higher
- **CUDA**: Optional, for GPU acceleration
- **Memory**: Minimum 4GB RAM (8GB+ recommended)
- **Storage**: 500MB for base installation, plus space for image/video storage

### Database Requirements
- **MongoDB**: Version 4.4 or higher
  - Local installation or cloud instance (Atlas)
  - MongoDB Compass (optional, for visual database management)

### Installation Methods

```bash
# macOS Installation (using Homebrew)
brew install mongodb/brew/mongodb-community
brew install python@3.8

# Ubuntu/Debian Installation
sudo apt-get update
sudo apt-get install -y mongodb python3.8 python3.8-venv

# Docker Installation (Alternative)
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

## ⚡ Quick Start Guide

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/anshika-ux/Coco_model_triple_riding_detection.git
cd Coco_model_triple_riding_detection

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Database Configuration
```bash
# Start MongoDB (macOS)
brew services start mongodb/brew/mongodb-community

# Start MongoDB (Linux)
sudo systemctl start mongod

# Verify MongoDB Connection
mongosh --eval "db.serverStatus()"
```

### 3. Model Setup
```bash
# Download YOLOv8 weights (if not present)
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt

# Verify model file
ls -l yolov8n.pt
```
## � Data Management

### MongoDB Integration

The system implements a robust data persistence layer using MongoDB:

#### Collection Architecture
- **Images Collection (`detections`)**
  - Stores individual image analysis results
  - Tracks violation statistics and metadata
  - Links to output files and annotations

- **Video Collection (`video_detections`)**
  - Manages frame-by-frame analysis data
  - Maintains video source references
  - Records temporal violation patterns

## 📊 Reports and Analytics

### CSV Reports
Generated automatically in output directories with columns:
- Image/Video identifier
- Total vehicles detected
- Total riders detected
- Number of violations
- Status (VIOLATION/COMPLIANT)

### Testing Framework

#### Image Detection Tests
```bash
# Basic detection test
python detect_triple_riding.py \
  --images datasets/triple_riding/images \
  --quiet

# Performance testing
python detect_triple_riding.py \
  --images datasets/triple_riding/images \
  --conf 0.5 \
  --show-confidence
```

#### Video Analysis Tests
```bash
# Frame extraction test
python detect_video_triple_riding.py \
  --file datasets/triple_riding/video/test.mp4 \
  --frame-interval 30 \
  --quiet

# Real-time processing test
python detect_video_triple_riding.py \
  --file test.mp4 \
  --show-confidence \
  --frame-interval 1
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is provided as-is under the MIT License. See LICENSE file for details.

## 📫 Support & Contact

### Getting Help
- [Open an Issue](https://github.com/anshika-ux/Coco_model_triple_riding_detection/issues)
- [Documentation Wiki](https://github.com/anshika-ux/Coco_model_triple_riding_detection/wiki)
- Email: [your-email@domain.com]

---

<div align="center">
Developed with ❤️ for Traffic Safety
</div>
