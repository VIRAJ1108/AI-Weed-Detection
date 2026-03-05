import cv2

def visualize_detections(image_path, detections, analysis, decision, output_path):

    image = cv2.imread(image_path)

    for d in detections:

        x1, y1, x2, y2 = map(int, d["bbox"])
        cls = d["class"]
        conf = d["confidence"]

        if cls == 0:
            label = "Crop"
            color = (0,255,0)   # green
        else:
            label = "Weed"
            color = (0,0,255)   # red

        cv2.rectangle(image, (x1,y1), (x2,y2), color, 2)

        text = f"{label} {conf:.2f}"

        cv2.putText(
            image,
            text,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            2
        )

    summary_text = f"Weeds: {analysis['weed_count']} | Crops: {analysis['crop_count']}"

    cv2.putText(
        image,
        summary_text,
        (20,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    cv2.putText(
        image,
        decision,
        (20,60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,255),
        2
    )

    cv2.imwrite(output_path, image)

    return image