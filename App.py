import streamlit as st
from ultralytics import YOLO
from PIL import Image, ImageDraw
from datetime import datetime
import pandas as pd

# -------------------------
# Initialize App State
# -------------------------
if "detection_results" not in st.session_state:
    st.session_state.detection_results = []

if "model" not in st.session_state:
    st.session_state.model = None

# -------------------------
# Human-Level Reasoning Layer (Simulated)
# -------------------------
def human_level_reasoning(label, confidence, context=""):
    """
    Simulates human-like reasoning: predicts category and handling instructions.
    Can be replaced with LLM API call for advanced predictions.
    """
    # Base mapping
    CATEGORY_MAP = {
        "plastic_bottle": "recyclable",
        "paper": "recyclable",
        "glass": "recyclable",
        "food": "organic",
        "banana_peel": "organic",
        "battery": "hazardous",
        "electronics": "hazardous",
        "other": "general"
    }
    INSTRUCTIONS = {
        "recyclable": "Wash if dirty and send to recycling bin.",
        "organic": "Compost or dispose in organic waste.",
        "hazardous": "Handle carefully with gloves and dispose safely.",
        "general": "Dispose in general waste bin."
    }
    
    category = CATEGORY_MAP.get(label, "general")
    
    # Simulate reasoning: context-aware adjustments
    if context.lower() in ["kitchen", "food waste"] and category == "organic":
        advice = "Compost immediately to prevent odor."
    elif category == "hazardous":
        advice = "Wear gloves and avoid contact. Dispose at hazardous waste center."
    else:
        advice = INSTRUCTIONS.get(category, "Dispose safely.")
    
    return category, advice

# -------------------------
# Streamlit App Components
# -------------------------
def header():
    st.title("Next-Gen Human-Level Waste Detection AI")
    st.markdown("**Detect, analyze, and handle waste like a human would!**")

def load_model():
    st.subheader("YOLOv8 Model")
    if st.button("Load Pre-trained YOLOv8 Model"):
        st.session_state.model = YOLO("yolov8n.pt")
        st.success("YOLOv8 loaded successfully!")

def upload_and_predict():
    uploaded_file = st.file_uploader("Upload a waste image", type=["jpg","png","jpeg"])
    context = st.text_input("Optional context (e.g., kitchen, street, industrial site)")
    
    if uploaded_file and st.session_state.model:
        image = Image.open(uploaded_file)
        st.write("Detecting waste...")
        
        results = st.session_state.model.predict(source=image, save=False)
        detections = []
        draw = ImageDraw.Draw(image)
        
        for r in results:
            for box, conf, cls in zip(r.boxes.xyxy, r.boxes.conf, r.boxes.cls):
                x1, y1, x2, y2 = map(int, box)
                label = st.session_state.model.names[int(cls)]
                
                # Human-level reasoning
                category, instruction = human_level_reasoning(label, float(conf), context)
                
                # Draw bounding box + human-like label
                draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
                draw.text((x1, y1-15), f"{label} ({category}) {conf:.2f}", fill="red")
                
                detections.append({
                    "label": label,
                    "category": category,
                    "confidence": float(conf),
                    "instruction": instruction,
                    "bbox": {"x": x1, "y": y1, "width": x2-x1, "height": y2-y1}
                })
        
        # Save detection
        result = {
            "id": str(len(st.session_state.detection_results)+1),
            "timestamp": datetime.now(),
            "image_name": uploaded_file.name,
            "detections": detections
        }
        st.session_state.detection_results.insert(0, result)
        st.session_state.detection_results = st.session_state.detection_results[:10]
        
        st.image(image, caption="Detection & Human-Level Classification")
        
        st.subheader("Human-Level Handling Instructions")
        for d in detections:
            st.write(f"{d['label']} → {d['category']} → {d['instruction']}")

def stats_panel():
    st.subheader("Detection Stats")
    total_images = len(st.session_state.detection_results)
    st.write(f"Total images processed: {total_images}")
    
    # Count categories
    category_counts = {}
    for res in st.session_state.detection_results:
        for d in res["detections"]:
            category_counts[d["category"]] = category_counts.get(d["category"], 0) + 1
    st.write("Category counts:", category_counts)

# -------------------------
# Main App
# -------------------------
def main():
    header()
    load_model()
    st.write("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        upload_and_predict()
    with col2:
        stats_panel()

if __name__ == "__main__":
    main()
