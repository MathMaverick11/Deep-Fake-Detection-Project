# 🎭 DeepFake Detector — Web App

> A browser-based image classification tool powered by **EfficientNet-B0**, engineered to accurately detect Real vs Fake (deepfake) face images with high confidence scoring.

![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=flat-square&logo=flask)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep_Learning-ee4c2c?style=flat-square&logo=pytorch)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## ✨ Features

- **🚀 Real-time Detection** — Instant classification with confidence scores
- **🎯 High Accuracy** — EfficientNet-B0 model trained on diverse facial datasets
- **🖥️ User-Friendly Interface** — Drag-and-drop upload with intuitive UI
- **📊 Confidence Visualization** — Probability bars for both Real/Fake classifications
- **⚡ Optimized Performance** — Lazy-loading model, minimal latency on subsequent requests
- **🔧 Flexible Infrastructure** — Auto GPU/CPU fallback, no additional setup required
- **📱 Responsive Design** — Works seamlessly on desktop and mobile browsers

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Flask 2.0+ |
| **Model** | EfficientNet-B0 (PyTorch) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Deep Learning** | PyTorch, torchvision |
| **Image Processing** | Pillow, OpenCV |
| **Python Version** | 3.8+ |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8** or newer
- **pip** (Python package manager)
- **Git** (optional, for cloning the repository)

---

## 🚀 Quick Start

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/deepfake-detector.git
cd deepfake-detector
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** On macOS or Linux, you might need to use `pip3` instead of `pip`.

### Step 3: Launch the Application

```bash
python app.py
```

You should see output similar to:

```
Loading model …
Model ready on cpu  |  Classes: ['Real', 'Fake']
 * Running on http://0.0.0.0:5000
```

### Step 4: Access the Web App

Open your browser and navigate to:

```
http://localhost:5000
```

---

## 📖 Usage Guide

### Basic Workflow

1. **Upload Image**
   - Drag and drop a face image onto the upload area, or click to browse your files
   
2. **Analyze**
   - Click the **Analyse Image** button to process the image
   
3. **View Results**
   - **Verdict** — Classification as Real or Fake with confidence percentage
   - **Confidence Bars** — Visual representation of probability for both classes

### Supported Formats & Constraints

| Property | Details |
|----------|---------|
| **Formats** | PNG, JPG, JPEG, WEBP |
| **Max File Size** | 10 MB |
| **Recommended Size** | 224×224 pixels (auto-resized) |
| **Face Requirements** | Clear, frontal face image for best results |

---

## 📁 Project Structure

```
deepfake-detector/
│
├── app.py                    # Flask backend & inference engine
├── best_model.pth           # Pre-trained EfficientNet-B0 model
├── requirements.txt         # Python dependencies
├── README.md                # This file
│
└── templates/
    └── index.html           # Frontend web interface
```

---

## 🔧 Configuration & Customization

### Changing the Server Port

If port 5000 is already in use, specify a different port:

```bash
python app.py --port 5001
```

### Model Details

- **Architecture:** EfficientNet-B0
- **Input Size:** 224×224 pixels
- **Normalization:** ImageNet statistics (mean, std)
- **Output Classes:** 
  - Class 0: **Real** (authentic faces)
  - Class 1: **Fake** (deepfake faces)
- **Inference Device:** Automatic GPU detection (falls back to CPU)

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: efficientnet_pytorch` | Run `pip install efficientnet-pytorch` |
| `Address already in use` | Change port: `python app.py --port 5001` or kill the process using the port |
| Slow initial request | Normal behavior — PyTorch loads lazily on first use; subsequent requests are faster |
| CUDA/GPU errors | App automatically falls back to CPU; no action required |
| `torch` import errors | Reinstall PyTorch: `pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu` |
| File upload fails | Ensure file size < 10 MB and format is PNG, JPG, or WEBP |

---

## ⚠️ Important Notes

- **Probabilistic Output** — The model returns confidence scores, not absolute guarantees. Always apply human judgment for critical decisions.
- **Data Privacy** — Uploaded images are processed locally and not stored on the server.
- **Best Results** — Model performs optimally on clear, frontal face images.
- **Model Limitations** — Performance may vary with highly edited, filtered, or low-resolution images.
- **Ethical Use** — Use this tool responsibly and in compliance with local laws and regulations.

---

## 📈 Performance Metrics

- **Model Size:** ~20 MB
- **Inference Time:** ~50-200ms (depending on hardware)
- **GPU Speedup:** 5-10x faster on NVIDIA/CUDA-enabled devices
- **Memory Usage:** ~500 MB (including model)

---

## 📝 Requirements File

Ensure your `requirements.txt` contains:

```
Flask>=2.0.0
PyTorch>=1.9.0
torchvision>=0.10.0
efficientnet-pytorch>=0.7.0
Pillow>=8.0.0
numpy>=1.19.0
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software for personal and commercial purposes.

---

## 🎓 References & Resources

- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Deepfake Detection: A Survey](https://arxiv.org/abs/2001.00686)


