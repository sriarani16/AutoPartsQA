import pandas as pd

CATEGORY_KEYWORDS = {
    "Engine": ["filter", "spark", "oil", "belt", "pump", "radiator"],
    "Brakes": ["brake", "pad", "disc", "rotor", "caliper"],
    "Suspension": ["shock", "strut", "spring", "suspension"],
    "Electrical": ["battery", "alternator", "sensor", "light", "lamp"],
    "Body": ["bumper", "mirror", "door", "fender", "grille"],
    "Transmission": ["clutch", "gear", "transmission", "axle"],
}

def detect_category(part_name):
    if not isinstance(part_name, str):
        return None

    name = part_name.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(word in name for word in keywords):
            return category

    return None  # fallback if no match


def apply_category_detection(df):
    df = df.copy()

    df["detected_category"] = df["part_name"].apply(detect_category)

    # If category column is missing or empty, fill it
    if "category" in df.columns:
        df["category"] = df["category"].fillna(df["detected_category"])
    else:
        df["category"] = df["detected_category"]

    return df
