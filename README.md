SmartWasteAI – AI-Powered Intelligent Waste Sorting System
(YOLOv8x + Python)
📌 Overview

SmartWasteAI is an AI-powered waste detection and classification system designed to automatically identify waste items and assign them to the correct disposal bins.
Using YOLOv8x for real-time object detection, the system contributes to smart-city sustainability by improving recycling efficiency and reducing manual sorting errors.

✅ Key Features

Real-time waste detection using YOLOv8x

Automatic bin classification using predefined bin rules

Confidence-based detection review

Annotated output image showing detected items and labels

Multi-class waste handling: Plastic, Metal, Organic, Paper, E-waste

Works seamlessly on Google Colab

Extendable to Streamlit or Flask for deployment

🔧 System Workflow

Problem Definition
Choose target waste categories: Plastic, Metal, Organic, Paper, E-Waste.

Data Handling
Uses pretrained YOLOv8x model trained on millions of COCO images.

Model Execution
Runs object detection on uploaded waste images.

Classification Logic
Matches each detected object to the appropriate waste bin.

Confidence Analysis
Displays confidence score for every prediction.

Visualization
Generates annotated images with bounding boxes and labels.

Testing & Evaluation
Tests the model on multiple unseen waste samples.

Deployment (Current)
Runs on Google Colab — ready for upgrade to a full web app.

🧠 Technical Implementation
Model

YOLOv8x.pt (pretrained)

Frameworks & Libraries

Ultralytics YOLO

Pillow

OpenCV

Matplotlib

Classification Rules
bins = {
    "Plastic Bin": ["bottle", "cup", "bag", "plastic", "container"],
    "Metal Bin": ["can", "metal", "tin", "spoon"],
    "Organic Bin": ["banana", "apple", "orange", "food", "vegetable", "fruit"],
    "Paper Bin": ["book", "cardboard", "paper", "newspaper"],
    "E-Waste Bin": ["laptop", "cell phone", "tv", "keyboard", "mouse"]
}

Confidence Threshold

0.4 (default)

Outputs

Annotated image of detections

Console summary of detected waste

Saved detection file (e.g., detected_waste.jpg)

📊 Evaluation Metrics

Accuracy based on confidence score

Precision & Recall using sample test images

Confusion Matrix to analyze classification performance

User Feedback from test users

📁 Repository Structure
SmartWasteAI/
│── SmartWasteAI_Code.py
│── dataset/
│── model/
│── results/
│── report/
│── README.txt

🚀 Future Enhancements

Display per-object confidence score in UI

Deploy using Streamlit for live webcam detection

Add analytics dashboard (bin-wise detection counts)

Add audio or color-coded feedback for different bins

Train YOLO on a custom waste dataset for improved accuracy

Expand categories for Indian/Asian waste items

🖼 Example Output (YOLOv8x Results)
Processing file: plastic_100.jpg

0: 640x640 3 bottles, 4179.8ms
Speed: 6.7ms preprocess, 4179.8ms inference, 14.0ms postprocess

SmartWasteAI - Waste Segregation Summary:
Plastic Bin: bottle, bottle, bottle

Saved annotated result as detected_plastic_100.jpg

▶️ Google Colab Notebook

You can run the full project here:
https://colab.research.google.com/drive/12hLcxkyBOTrIcTtkhPuRbN9KzWGcdEbj#scrollTo=Yin3CWsexrMa
