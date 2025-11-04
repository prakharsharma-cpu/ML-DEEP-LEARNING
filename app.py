import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

# Set page title and layout
st.set_page_config(page_title="♻️ SmartWasteAI – AI Waste Segregation System", layout="centered")
st.title("♻️ SmartWasteAI – AI Waste Segregation System")

# Load YOLO model safely
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# File uploader
uploaded_file = st.file_uploader("📸 Upload a waste image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Read image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="🖼 Uploaded Image", use_container_width=True)

    # Convert PIL to numpy
    image_np = np.array(image)

    # Run YOLO prediction
    results = model.predict(image_np)
    result = results[0]

    if len(result.boxes) == 0:
        st.warning("⚠️ No objects detected. Please try another image.")
    else:
        # Extract first detection info
        cls_id = int(result.boxes.cls[0])
        conf = float(result.boxes.conf[0])
        label = model.names[cls_id]

        # Function to decide bin type
        def get_bin_color(waste_type):
            if waste_type.lower() in ['food', 'paper', 'leaf']:
                return '🟢 Green Bin (Biodegradable)'
            elif waste_type.lower() in ['plastic', 'glass', 'metal']:
                return '🔵 Blue Bin (Recyclable)'
            else:
                return '🔴 Red Bin (Hazardous)'

        st.subheader("🔍 Detection Result")
        st.write(f"**Waste Type:** {label}")
        st.write(f"**Confidence:** {conf:.2f}")
        st.write(f"**Recommended Bin:** {get_bin_color(label)}")

        # Show annotated image
        annotated_image = result.plot()
        st.image(annotated_image, caption="✅ Detected Waste", use_container_width=True)
