import pandas as pd

BRAND_MAP = {
    "Toyta": "Toyota",
    "Tyoata": "Toyota",
    "Hunda": "Honda",
    "Hondaa": "Honda",
    "Nisssan": "Nissan",
    "Nisan": "Nissan",
    "BMWM": "BMW",
    "BMM": "BMW",
    "Frod": "Ford",
    "Fo rd": "Ford",
}

def clean_brand(df):
    df = df.copy()
    df["manufacturer"] = df["manufacturer"].apply(
        lambda x: BRAND_MAP.get(x, x) if isinstance(x, str) else x
    )
    return df
