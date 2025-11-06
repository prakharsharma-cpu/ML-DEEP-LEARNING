# ♻️ SmartWasteAI - Advanced Waste Segregation System (YOLOv8x)
# Uses the YOLOv8x pretrained model trained on millions of images
# No Streamlit, fully works in Google Colab

# --- Step 1: Install libraries ---
!pip install ultralytics pillow matplotlib opencv-python

# --- Step 2: Import required packages ---
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
from google.colab import files

# --- Step 3: Load YOLOv8x (largest, most accurate pretrained model) ---
model = YOLO('yolov8x.pt')  # "x" = extra-large, trained on millions of COCO images
print("✅ Loaded YOLOv8x model — high accuracy, pretrained on millions of samples!")

# --- Step 4: Define smart bin rules ---
bins = {
    "Plastic Bin": ["bottle", "cup", "bag", "plastic", "container"],
    "Metal Bin": ["can", "metal", "tin", "spoon"],
    "Organic Bin": ["banana", "apple", "orange", "food", "vegetable", "fruit"],
    "Paper Bin": ["book", "cardboard", "paper", "newspaper"],
    "E-Waste Bin": ["laptop", "cell phone", "tv", "keyboard", "mouse"]
}

def assign_bin(label):
    """Assign detected label to the correct bin."""
    for bin_name, keywords in bins.items():
        if any(keyword in label.lower() for keyword in keywords):
            return bin_name
    return "Other Waste Bin"

# --- Step 5: Upload image(s) ---
print("\n📤 Please upload one or more waste images to analyze:")
uploaded = files.upload()

# --- Step 6: Process and classify ---
for filename in uploaded.keys():
    print(f"\n📁 Processing file: {filename}")

    # Open image
    img = Image.open(filename)
    # Convert to RGB to ensure 3 channels
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    img_np = np.array(img)

    # 🧠 Run high-accuracy detection
    results = model.predict(img_np, conf=0.4)
    annotated_img = results[0].plot()

    # Extract detections
    detected_items = results[0].boxes.cls
    names = results[0].names
    bin_summary = {}

    # Assign detected objects to bins
    for cls_id in detected_items:
        label = names[int(cls_id)]
        bin_type = assign_bin(label)
        bin_summary.setdefault(bin_type, []).append(label)

    # --- Step 7: Display results ---
    print("\n♻️ SmartWasteAI - Waste Segregation Summary:")
    if bin_summary:
        for bin_type, items in bin_summary.items():
            print(f"🗑️ {bin_type}: {', '.join(items)}")
    else:
        print("⚠️ No recognizable waste objects detected.")

    # Show annotated detection image
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("SmartWasteAI - YOLOv8x Detection & Waste Bin Classification")
    plt.show()

    # Save output
    output_path = f"detected_{filename}"
    cv2.imwrite(output_path, annotated_img)
    print(f"💾 Saved annotated result as {output_path}")
