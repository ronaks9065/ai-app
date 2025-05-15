# import streamlit as st
# from PIL import Image
 
# st.title("📷 Image Uploader")
 
# uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
 
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_column_width=True)


import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np

# Initialize YOLO model
@st.cache_resource
def load_model():
    return YOLO("yolo11s-cls.pt")  # pretrained YOLO11n model

model = load_model()

st.title("📷 Image Classification with YOLO")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Save uploaded image temporarily for YOLO processing
    # temp_image_path = "temp_image.png"
    # image.save(temp_image_path)
    
    # Run inference
    results = model([image])
    
    # Process results
    for result in results:
        # Get probabilities
        probs = result.probs
        # Get the index of the class with highest confidence
        top1_idx = probs.top1
        # Get the confidence score
        top1_conf = probs.top1conf.item()
        # Get class name
        class_name = model.names[top1_idx]
        
        # Display result
        st.write(f"**Predicted Class**: {class_name}")
        st.write(f"**Confidence Score**: {top1_conf:.3f}")