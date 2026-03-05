from ultralytics import YOLO

class WeedDetector:

    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, image_path):

        results = self.model(image_path, conf=0.35)

        detections = []

        r = results[0]

        if r.boxes is None:
            return detections

        for box in r.boxes:

            cls = int(box.cls.item())
            conf = float(box.conf.item())

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            detections.append({
                "class": cls,
                "confidence": conf,
                "bbox": [x1, y1, x2, y2]
            })

        return detections