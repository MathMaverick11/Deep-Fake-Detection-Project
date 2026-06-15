import os
import io
import base64
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, request, jsonify, render_template
from efficientnet_pytorch import EfficientNet

app = Flask(__name__)

# ── Model configuration ──────────────────────────────────────────────────────
CLASS_NAMES = ['Real', 'Fake']
DEVICE      = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
MODEL_PATH  = os.path.join(os.path.dirname(__file__), 'best_model.pth')

# ── Build model identical to training ────────────────────────────────────────
def build_model():
    base = EfficientNet.from_name('efficientnet-b0')
    in_features = base._fc.in_features
    # Indices 1 & 4 match the saved checkpoint (built with a leading placeholder at 0)
    base._fc = nn.Sequential(
        nn.Identity(),           # index 0 – placeholder
        nn.Linear(in_features, 256),  # index 1
        nn.ReLU(),               # index 2
        nn.Dropout(0.5),         # index 3
        nn.Linear(256, 2),       # index 4
    )
    return base

def load_model():
    model = build_model()
    checkpoint = torch.load(MODEL_PATH, map_location=DEVICE, weights_only=False)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.to(DEVICE)
    model.eval()
    return model

print("Loading model …")
model = load_model()
print(f"Model ready on {DEVICE}  |  Classes: {CLASS_NAMES}")

# ── Image preprocessing ───────────────────────────────────────────────────────
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Read and preprocess
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
        tensor = transform(img).unsqueeze(0).to(DEVICE)

        # Inference
        with torch.no_grad():
            logits = model(tensor)
            probs  = torch.softmax(logits, dim=1)[0]

        real_conf = round(probs[0].item() * 100, 2)
        fake_conf = round(probs[1].item() * 100, 2)
        label     = 'Real' if real_conf > fake_conf else 'Fake'

        # Thumbnail for preview
        img.thumbnail((400, 400))
        buf = io.BytesIO()
        img.save(buf, format='JPEG', quality=85)
        img_b64 = base64.b64encode(buf.getvalue()).decode()

        return jsonify({
            'label':     label,
            'real_conf': real_conf,
            'fake_conf': fake_conf,
            'image':     img_b64,
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
