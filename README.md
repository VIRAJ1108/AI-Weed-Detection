SmartSpray AI – Crop vs Weed Detection System
Overview

SmartSpray AI is a computer vision system designed for precision agriculture, capable of detecting crops and weeds from field images and providing spray recommendations based on weed density.

The system uses a deep learning object detection model to identify weeds and crops, analyze their distribution in the field, and generate a spraying recommendation to help reduce herbicide usage and improve crop management.

This project demonstrates a complete applied AI pipeline including model training, computer vision inference, decision logic, visualization, and deployment as a web application.

Live Demo

Try the application here:
https://ai-weed-detection-s4yvreol6c8sgxhymsjzoy.streamlit.app/

Users can upload a field image and the system will:

Detect crops and weeds

Display bounding boxes around detected plants

Calculate weed density

Generate a spraying recommendation

Model

The detection model is trained using the YOLO architecture from the Ultralytics framework.

Key characteristics:

Object detection based plant classification

Two detection classes:

Crop

Weed

Optimized for detecting small plants in agricultural fields

