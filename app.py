from __future__ import division, print_function
import os
import torch
from torch import nn
from torchvision import models, transforms
from PIL import Image
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

# Flask app initialization
app = Flask(__name__)

# Model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pth')

# Check device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the model architecture and weights
model = models.resnet18(weights='DEFAULT')
model.fc = nn.Linear(in_features=512, out_features=4)  # Update for your classification task
model = model.to(device)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.eval()

# Define image transformation
image_transforms = transforms.Compose([
    transforms.Resize((256, 256)),  # Resize to match model input size
    transforms.ToTensor(),          # Convert to tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225])  # Normalize
])

# Prediction function
def model_predict(img_path, model):
    # Load image
    img = Image.open(img_path).convert('RGB')  # Ensure image is RGB

    # Transform the image
    img = image_transforms(img).unsqueeze(0).to(device)  # Add batch dimension

    # Perform prediction
    with torch.no_grad():
        preds = model(img)
        predicted_class = preds.argmax(dim=1).item()  # Get the class with the highest score

    return predicted_class

# Flask routes
@app.route('/')
def index():
    # Main page
    return render_template('home.html')
@app.route('/detect-disease')
def detect():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Ensure 'file' is in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        f = request.files['file']

        # Ensure a file was selected
        if f.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Save the file to the uploads directory
        basepath = os.path.dirname(__file__)
        upload_folder = os.path.join(basepath, 'uploads')
        os.makedirs(upload_folder, exist_ok=True)  # Ensure the directory exists
        file_path = os.path.join(upload_folder, secure_filename(f.filename))
        f.save(file_path)

        # Perform prediction
        try:
            predicted_class = model_predict(file_path, model)

            # Optional: Map predicted class index to a human-readable label
            CLASS_LABELS = {
                0: 'Healthy',
                1: 'Corn Leaf Blight',
                2: 'Common Rust',
                3: 'Gray Leaf Spot'
            }
            predicted_label = CLASS_LABELS.get(predicted_class, 'Unknown')

            # Return the prediction result
            result = {'predicted_class': predicted_class, 'predicted_label': predicted_label}
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        # Clean up uploaded file
        if os.path.exists(file_path):
            os.remove(file_path)

        return jsonify(result)

    return "Please upload an image.", 400

if __name__ == '_main_':
    app.run(debug=True)