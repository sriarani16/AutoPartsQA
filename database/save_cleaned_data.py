from sqlalchemy import create_engine
import time

def save_cleaned_data(df):
    engine = create_engine("postgresql://postgres:admin123@localhost:5432/autopartsqa")

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    table_name = f"parts_cleaned_{timestamp}"
    print("Using timestamp save function:", table_name)

    df.to_sql(table_name, engine, if_exists="replace", index=False)
    return table_name
