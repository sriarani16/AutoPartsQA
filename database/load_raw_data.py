import pandas as pd
from sqlalchemy import create_engine

def load_raw_data():
    engine = create_engine("postgresql://postgres:admin123@localhost:5432/autopartsqa")
    df = pd.read_sql("SELECT * FROM parts;", engine)
    return df
