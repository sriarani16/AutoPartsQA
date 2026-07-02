from sqlalchemy import create_engine
import pandas as pd

def load_from_postgres():
    engine = create_engine("postgresql://postgres:admin123@localhost:5432/autopartsqa")
    query = "SELECT * FROM parts;"
    df = pd.read_sql(query, engine)
    return df
