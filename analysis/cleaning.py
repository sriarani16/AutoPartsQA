import pandas as pd
import numpy as np

DATA_PATH = "data/parts.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

def basic_profile(df):
    print("Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nHead:")
    print(df.head())
    print("\nMissing values per column:")
    print(df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

if __name__ == "__main__":
    df = load_data()
    basic_profile(df)
