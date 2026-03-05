import streamlit as st
import cv2
import tempfile
from src.detect import WeedDetector
from src.weed_analysis import analyze_detections
from src.spray_logic import spray_decision
from src.visualize import visualize_detections

MODEL_PATH = "models/best_weed.pt"

st.title("SmartSpray AI - Crop vs Weed Detection")

st.write("Upload a field image to detect weeds and generate spray recommendations.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    tfile = tempfile.NamedTemporaryFile(delete=False,suffix=".jpg")
    tfile.write(uploaded_file.read())

    detector = WeedDetector(MODEL_PATH)

    detections = detector.detect(tfile.name)

    analysis = analyze_detections(detections)

    decision = spray_decision(analysis["weed_density"])

    output_path = "outputs/result.jpg"

    visualize_detections(
        tfile.name,
        detections,
        analysis,
        decision,
        output_path
    )

    image = cv2.imread(output_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    st.image(image, caption="Detection Result")

    st.subheader("Analysis")

    st.write(f"Crops detected: {analysis['crop_count']}")
    st.write(f"Weeds detected: {analysis['weed_count']}")
    st.write(f"Weed density: {round(analysis['weed_density'],2)}")

    st.subheader("Recommendation")

    st.success(decision)

