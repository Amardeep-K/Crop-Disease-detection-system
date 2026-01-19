# Corn Leaf Disease Detection System 🌽🛡️

A Deep Learning-based web application that identifies diseases in corn leaves using **PyTorch** and **Flask**. The system uses a ResNet-based model trained to detect multiple categories of corn health.

## 🚀 Features
- **Real-time Detection:** Upload an image of a corn leaf and get instant diagnosis.
- **Deep Learning Core:** Built using a ResNet architecture for high-accuracy image classification.
- **Web Interface:** User-friendly UI built with Flask, HTML5, and CSS3.

## 🛠️ Tech Stack
- **Framework:** Flask
- **Machine Learning:** PyTorch, Torchvision
- **Language:** Python 3.12
- **Frontend:** HTML, CSS, JavaScript

## 📦 Installation & Setup

1. **Clone the Repository:**
   \`\`\`bash
   git clone https://github.com/Amardeep-K/Crop-Disease-detection-system.git
   cd Crop-Disease-detection-system
   \`\`\`

2. **Create a Virtual Environment:**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

3. **Install Dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run the Application:**
   \`\`\`bash
   python app.py
   \`\`\`

## 📂 Project Structure
\`\`\`text
├── app.py              # Flask Application logic
├── model.pth           # Trained PyTorch Model (via Git LFS)
├── static/             # CSS, JS, and Images
├── templates/          # HTML Templates
└── requirements.txt    # Project Dependencies
\`\`\`

