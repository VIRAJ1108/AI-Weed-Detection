import os
from src.detect import WeedDetector
from src.weed_analysis import analyze_detections
from src.spray_logic import spray_decision
from src.visualize import visualize_detections

MODEL_PATH = "models/best_weed.pt"
IMAGE_FOLDER = "sample_images"
OUTPUT_FOLDER = "outputs"

detector = WeedDetector(MODEL_PATH)

for image_name in os.listdir(IMAGE_FOLDER):
    image_path = os.path.join(IMAGE_FOLDER, image_name)

    if not image_path.lower().endswith((".jpg",".jpeg",".png")):
        continue
    
    output_path = os.path.join(OUTPUT_FOLDER, image_name)

    detections = detector.detect(image_path)

    analysis = analyze_detections(detections)

    decision = spray_decision(analysis["weed_density"])

    visualize_detections(
        image_path,
        detections,
        analysis,
        decision,
        output_path   
        )

    print("\nProcessing:", image_name)

    print("Crops detected:", analysis["crop_count"])
    print("Weeds detected:", analysis["weed_count"])
    print("Weed density:", round(analysis["weed_density"],2))

    print("Recommendation:", decision)

print("\nBatch processing complete.")