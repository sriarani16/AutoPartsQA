import pandas as pd

def calculate_quality_score(df):
    total_rows = len(df)
    total_cells = total_rows * len(df.columns)

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()
    invalid_prices = (df["price"] <= 0).sum()

    score = 100
    score -= (missing / total_cells) * 40
    score -= (duplicates / total_rows) * 30
    score -= (invalid_prices / total_rows) * 30

    return round(score, 2)
