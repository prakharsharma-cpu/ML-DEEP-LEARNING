pip install ultralytics

import streamlit as st
from ultralytics import YOLO
from PIL import Image


model = YOLO('best.pt')  # your trained model


st.title("♻️ SmartWasteAI – AI Waste Segregation System")

uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "jpeg", "png"])


if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    results = model.predict(image)

    result = results[0]

    cls_id = int(result.boxes.cls[0])

    label = model.names[cls_id]

    conf = float(result.boxes.conf[0])

    

    def get_bin_color(waste_type):

        if waste_type in ['food', 'paper', 'leaf']:

            return 'Green Bin (Biodegradable)'

        elif waste_type in ['plastic', 'glass', 'metal']:

            return 'Blue Bin (Recyclable)'

        else:

            return 'Red Bin (Hazardous)'

    

    st.write(f"### Waste Type: {label}")

    st.write(f"### Confidence: {conf:.2f}")

    st.write(f"### Recommended Bin: {get_bin_color(label)}")
