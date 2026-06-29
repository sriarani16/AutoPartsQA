import pandas as pd
import numpy as np

DATA_PATH = "data/parts.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

def detect_duplicates(df):
    dup_mask = df.duplicated()
    return df[dup_mask]

def detect_missing_values(df):
    return df.isnull().sum()

def detect_missing_brands(df):
    return df[df["Brand"].isnull() | (df["Brand"] == "")]

def detect_missing_vehicles(df):
    return df[df["Vehicle"].isnull() | (df["Vehicle"] == "")]

def detect_invalid_prices(df):
    invalid_rows = []
    for idx, value in df["Price"].items():
        try:
            price = float(value)
            if price <= 0:
                invalid_rows.append(idx)
        except:
            invalid_rows.append(idx)
    return df.loc[invalid_rows]

def detect_spelling_issues(df):
    known_brands = ["Toyota", "Honda", "Ford", "BMW", "Nissan"]
    mask = ~df["Brand"].isin(known_brands) & df["Brand"].notnull() & (df["Brand"] != "")
    return df[mask]

def compute_quality_score(df):
    total_rows = len(df)

    duplicates = len(detect_duplicates(df))
    missing_vals = detect_missing_values(df).sum()
    invalid_prices = len(detect_invalid_prices(df))
    missing_brands = len(detect_missing_brands(df))
    missing_vehicles = len(detect_missing_vehicles(df))
    spelling_issues = len(detect_spelling_issues(df))

    penalty = (
        duplicates +
        missing_vals +
        invalid_prices * 2 +
        missing_brands +
        missing_vehicles +
        spelling_issues
    )

    score = max(0, 100 - (penalty / max(total_rows, 1)) * 10)
    return round(score, 2)

if __name__ == "__main__":
    df = load_data()
    print("Total parts:", len(df))
    print("Duplicate records:", len(detect_duplicates(df)))
    print("Missing brands:", len(detect_missing_brands(df)))
    print("Missing vehicle models:", len(detect_missing_vehicles(df)))
    print("Invalid prices:", len(detect_invalid_prices(df)))
    print("Spelling issues:", len(detect_spelling_issues(df)))
    print("Overall data quality:", compute_quality_score(df), "%")
