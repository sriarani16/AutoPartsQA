

import pandas as pd

def clean_data(df):
    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Rename to expected names
    df = df.rename(columns={
        "brand": "manufacturer",
        "vehicle": "model",
        "partname": "part_name"
    })

    # Convert price to numeric (invalid → NaN)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Remove duplicates
    df = df.drop_duplicates()

    # Drop rows missing key fields
    df = df.dropna(subset=["manufacturer", "model", "part_name"])

    # Remove invalid prices (<= 0)
    df["price"] = df["price"].apply(lambda x: x if x and x > 0 else None)

    return df
