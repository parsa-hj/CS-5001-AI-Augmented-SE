def rgb_to_hsv(r, g, b):
    # Normalize RGB values to [0, 1] range
    r_normalized = r / 255.0
    g_normalized = g / 255.0
    b_normalized = b / 255.0

    max_val = max(r_normalized, g_normalized, b_normalized)
    min_val = min(r_normalized, g_normalized, b_normalized)
    delta = max_val - min_val

    # Calculate Hue
    if max_val == min_val:
        hue = 0
    elif max_val == r_normalized:
        hue = (60 * ((g_normalized - b_normalized) / delta) + 360) % 360
    elif max_val == g_normalized:
        hue = (60 * ((b_normalized - r_normalized) / delta) + 120) % 360
    elif max_val == b_normalized:
        hue = (60 * ((r_normalized - g_normalized) / delta) + 240) % 360

    # Calculate Saturation
    saturation = 0 if max_val == 0 else (delta / max_val) * 100

    # Calculate Value
    value = max_val * 100

    return hue, saturation, value
