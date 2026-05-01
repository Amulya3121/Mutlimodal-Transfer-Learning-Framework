# Multimodal Transfer Learning Framework for Automated Detection of Goitre and Thyroid Tumours in Ultrasound Imaging

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-PyTorch-orange?logo=pytorch)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-yellow)

> A multimodal, transfer-learning-based diagnostic system that combines **ultrasound imaging**, **textual radiology descriptions**, and **clinical tabular data** for accurate thyroid lesion classification and localization.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Modules](#modules)
- [Algorithms Used](#algorithms-used)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Authors](#authors)
- [References](#references)

---

## Overview

Thyroid disorders such as **diffuse goitre** and **thyroid tumours** are among the most prevalent endocrine diseases. Early detection is critical for effective treatment. This project presents an automated diagnostic framework that:

- Processes **thyroid ultrasound images** using deep learning models enhanced with transfer learning
- Analyzes **voice/acoustic signals** to extract physiological biomarkers
- Fuses multimodal features using a **cross-modal transformer fusion** module
- Classifies thyroid conditions into: `Normal`, `Diffuse Goitre`, `Thyroid Tumour`

The system outperforms conventional image-only YOLO baselines by incorporating supplementary clinical context, achieving higher sensitivity for small lesions and better boundary distinction under noisy ultrasound conditions.

---

## Features

- Multimodal input — ultrasound images + voice samples + clinical metadata
- Transfer learning from large-scale medical datasets (VGGNet, ResNet)
- C2fA attention module for robust spatial feature extraction
- Cross-modal transformer fusion for complementary representation learning
- Modality-aligned contrastive learning for noise robustness
- Real-time detection with bounding boxes and confidence scores
- Scalable for clinical and telemedicine settings

---

## System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  PRESENTATION LAYER                 │
│         Upload Interface (Ultrasound + Voice)       │
└───────────────────────┬─────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────┐
│                  PROCESSING LAYER                   │
│                                                     │
│  ┌──────────────────┐    ┌───────────────────────┐  │
│  │ Ultrasound       │    │  Voice Analysis       │  │
│  │ Analysis Module  │    │  Module               │  │
│  │ (VGGNet/ResNet + │    │  (Temporal & Spectral │  │
│  │  Transfer Learn) │    │   Features)           │  │
│  └────────┬─────────┘    └───────────┬───────────┘  │
│           │                          │              │
│           └──────────┬───────────────┘              │
│                      ▼                              │
│          ┌───────────────────────┐                  │
│          │  Feature Fusion       │                  │
│          │  Module (Cross-Modal  │                  │
│          │  Transformer)         │                  │
│          └───────────┬───────────┘                  │
│                      ▼                              │
│          ┌───────────────────────┐                  │
│          │  Classification       │                  │
│          │  Module               │                  │
│          │  Normal / Goitre /    │                  │
│          │  Tumour               │                  │
│          └───────────────────────┘                  │
└───────────────────────┬─────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────┐
│                   STORAGE LAYER                     │
│           Medical Data Repository                   │
│    (Images, Features, Predictions, Records)         │
└─────────────────────────────────────────────────────┘
```

---

## Modules

| Module | Description |
|---|---|
| **Presentation Module** | Web-based interface for uploading ultrasound images and voice samples; displays results with confidence scores |
| **Ultrasound Analysis Module** | Extracts spatial and texture features using VGGNet/ResNet with transfer learning; handles speckle noise and low contrast |
| **Voice Analysis Module** | Analyzes acoustic signals to detect physiological changes associated with thyroid abnormalities |
| **Feature Fusion Module** | Learns cross-modal relationships and generates a unified discriminative feature vector |
| **Classification Module** | Classifies into `Normal`, `Diffuse Goitre`, or `Thyroid Tumour` with improved accuracy |
| **Medical Data Repository** | Securely stores all data, features, and predictions for future analysis and model retraining |

---

## Algorithms Used

### 1. VGGNet — Ultrasound Image Feature Extraction
Uses a deep architecture with small convolutional filters to capture fine-grained texture variations and structural patterns. Fine-tuned on thyroid datasets via transfer learning.

### 2. ResNet — Deep Feature Learning
Employs residual skip connections to mitigate the vanishing gradient problem, enabling stable training of deeper networks for detecting subtle tumour boundaries and gland enlargement.

### 3. CNN with Transfer Learning
Pretrained models are fine-tuned on thyroid ultrasound images, reusing low-level feature representations for faster convergence on limited medical data.

### 4. Cross-Modal Transformer Fusion
Aligns and fuses ultrasound image features with voice features and clinical metadata to learn complementary representations.

### 5. Contrastive Learning (SimCLR-inspired)
Modality-aligned contrastive learning increases model robustness against noise and class imbalance.

---

## Dataset

- Combined thyroid ultrasound dataset with annotations for:
  - Normal thyroid
  - Diffuse goitre
  - Focal thyroid tumours
- Augmented with patient clinical data: **age**, **TSH/T3/T4 levels**, **nodule history**
- Paired with **radiology text descriptions** for multimodal fusion

> ⚠️ Dataset access may be restricted due to medical data privacy regulations. Contact the authors for details.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Amulya3121/multimodal-Transfer-Learning-Framework.git
cd multimodal-thyroid-detection

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Requirements (`requirements.txt`)

```
torch>=1.12.0
torchvision>=0.13.0
numpy>=1.21.0
opencv-python>=4.5.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
librosa>=0.9.0
pandas>=1.3.0
Pillow>=8.3.0
tqdm>=4.62.0
```

---

## Usage

### 1. Preprocess Data
```bash
python preprocess.py --image_dir data/ultrasound/ --voice_dir data/voice/ --output_dir data/processed/
```

### 2. Train the Model
```bash
python train.py --epochs 50 --batch_size 16 --lr 0.001 --modality multimodal
```

### 3. Evaluate
```bash
python evaluate.py --checkpoint checkpoints/best_model.pth --test_dir data/test/
```

### 4. Run Inference (Single Sample)
```bash
python infer.py --image path/to/ultrasound.jpg --voice path/to/voice.wav
```

### 5. Launch Web Interface
```bash
python app.py
```
Then navigate to `http://localhost:5000` in your browser.

---

## Results

| Metric | Image-Only Baseline | Proposed Multimodal |
|---|---|---|
| Accuracy | ~84% | **~93%** |
| Precision | ~82% | **~91%** |
| Recall | ~80% | **~92%** |
| F1-Score | ~81% | **~91%** |

- Consistent training/validation convergence with minimal overfitting
- Strong diagonal values in confusion matrix indicating high true positive rates
- Real-time bounding box detection with confidence scores
- Higher sensitivity for small lesions under challenging ultrasound conditions

---

---

## Authors

| Name | Institution | Email |
|---|---|---|
| Yanamadala Lakshmi Sri Priya | NRI Institute of Technology, Vijayawada | lakshmisripriya.y@gmail.com |
| Peeka Amulya | NRI Institute of Technology, Gannavaram | amulyapeeka2005@gmail.com |
| Velagapudi Venkata Dinesh | NRI Institute of Technology, Kavuluru | dineshchowdary123987@gmail.com |
| Polavarapu Naga Rohith | NRI Institute of Technology, Vijayawada | polavarapunagarohith@gmail.com |
| Santhi Chavala *(Corresponding)* | NRI Institute of Technology, Vijayawada | shantichavala@gmail.com |

---

## References

1. Haugen H. R. et al., "2015 American Thyroid Association management guidelines," *Thyroid*, vol. 26, no. 1, 2016.
2. World Health Organization, "Global prevalence of thyroid disorders," WHO Press, 2022.
3. Singh S. et al., "Deep learning-based classification of thyroid nodules," *IEEE Access*, vol. 8, 2020.
4. Redmon J. and Farhadi A., "YOLOv3: An incremental improvement," *arXiv:1804.02767*, 2018.
5. Jocher G. et al., "YOLOv5: Real-time object detection," Ultralytics, 2022.
6. Liu L. et al., "Swin Transformer: Hierarchical vision transformer using shifted windows," *IEEE/CVF ICCV*, 2021.
7. Gao Y. et al., "Cross-modal attention transformers for multimodal medical image analysis," *IEEE TMI*, vol. 41, 2022.
8. Dosovitskiy et al., "An image is worth 16×16 words: Transformers for image recognition at scale," *ICLR*, 2021.
9. Chen T. et al., "A simple framework for contrastive learning of visual representations," *ICML*, 2020.
10. Liu X. et al., "Multimodal learning for medical image analysis: A survey," *Medical Image Analysis*, vol. 80, 2022.

---


## Acknowledgements

This work was conducted at the **Department of Computer Science & Engineering, NRI Institute of Technology**, Andhra Pradesh, India. We acknowledge the open-source deep learning communities and medical imaging researchers whose prior work made this research possible.

---

