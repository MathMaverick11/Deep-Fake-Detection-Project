# DeepFake Detector — Web App

A browser-based image classification tool powered by **EfficientNet-B0**,
trained to detect Real vs Fake (deepfake) face images.

---

## 📁 Project Structure

```
deepfake_detector/
├── app.py              ← Flask backend + inference logic
├── best_model.pth      ← Your trained EfficientNet model
├── requirements.txt    ← Python dependencies
├── templates/
│   └── index.html      ← Frontend web page
└── README.md
```

---

## ⚙️ Setup & Run

### 1 — Prerequisites
- Python 3.8 or newer
- pip

### 2 — Install dependencies
Open a terminal inside the `deepfake_detector/` folder and run:

```bash
pip install -r requirements.txt
```

> On some systems use `pip3` instead of `pip`.

### 3 — Start the server
```bash
python app.py
```

You should see output like:
```
Loading model …
Model ready on cpu  |  Classes: ['Real', 'Fake']
 * Running on http://0.0.0.0:5000
```

### 4 — Open the web app
Open your browser and go to:

```
http://localhost:5000
```

---

## 🖼️ How to use

1. Drag & drop a face image onto the upload area (or click to browse).
2. Click **Analyse Image**.
3. The app returns:
   - **Verdict** — Real or Fake with confidence percentage.
   - **Confidence bars** — probability for both classes.

Supported formats: PNG, JPG, WEBP (max 10 MB).

---

## 🔧 Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: efficientnet_pytorch` | Run `pip install efficientnet-pytorch` |
| `Address already in use` | Change port: `python app.py --port 5001` (or kill the other process) |
| Slow on first request | Normal — PyTorch loads lazily; subsequent requests are faster |
| CUDA / GPU errors | The app auto-falls back to CPU; no action needed |

---

## 📝 Notes

- The model uses **EfficientNet-B0** with a custom two-class head.
- Input images are resized to **224×224** and normalised with ImageNet stats.
- Classes: **Real** (index 0) and **Fake** (index 1).
- Results are probabilistic; always apply human judgment for critical decisions.
