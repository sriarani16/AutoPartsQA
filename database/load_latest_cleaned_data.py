import pandas as pd
from sqlalchemy import create_engine, text

def load_latest_cleaned_data():
    engine = create_engine("postgresql://postgres:admin123@localhost:5432/autopartsqa")

    # Find latest cleaned table
    query = text("""
        SELECT tablename
        FROM pg_tables
        WHERE schemaname = 'public'
          AND tablename LIKE 'parts_cleaned_%'
        ORDER BY tablename DESC
        LIMIT 1;
    """)

    with engine.connect() as conn:
        result = conn.execute(query).fetchone()

    if not result:
        return None  # No cleaned tables found

    latest_table = result[0]

    df = pd.read_sql(f"SELECT * FROM {latest_table};", engine)
    return df

