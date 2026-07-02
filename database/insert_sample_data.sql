import pandas as pd
from sqlalchemy import create_engine

def insert_sample_data():
    engine = create_engine("postgresql://postgres:admin123@localhost:5432/autopartsqa")

    df = pd.read_csv("data/parts.csv")

    df.to_sql("parts", engine, if_exists="replace", index=False)
    print(f"Inserted {len(df)} rows into 'parts' table.")

if __name__ == "__main__":
    insert_sample_data()
