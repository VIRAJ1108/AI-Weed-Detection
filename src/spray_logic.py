def spray_decision(weed_density):

    if weed_density == 0:
        return "No spraying required"

    if weed_density < 0.2:
        return "Low intensity targeted spray"

    if weed_density < 0.5:
        return "Moderate spraying required"

    return "High weed infestation - aggressive spraying"