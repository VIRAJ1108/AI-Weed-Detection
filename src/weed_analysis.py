def analyze_detections(detections):

    crop_count = 0
    weed_count = 0

    for d in detections:

        if d["class"] == 0:
            crop_count += 1
        else:
            weed_count += 1

    total = crop_count + weed_count

    weed_density = 0

    if total > 0:
        weed_density = weed_count / total

    return {
        "crop_count": crop_count,
        "weed_count": weed_count,
        "weed_density": weed_density
    }