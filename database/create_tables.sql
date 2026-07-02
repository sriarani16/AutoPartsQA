from sqlalchemy import create_engine, text

def create_tables():
    engine = create_engine("postgresql://postgres:admin123@localhost:5432/autopartsqa")

    schema_sql = """
    CREATE TABLE IF NOT EXISTS parts (
        part_id        INTEGER PRIMARY KEY,
        manufacturer   VARCHAR(100),
        model          VARCHAR(100),
        category       VARCHAR(100),
        part_name      VARCHAR(200),
        price          NUMERIC
    );
    """

    with engine.connect() as conn:
        conn.execute(text(schema_sql))
        conn.commit()

    print("Tables created successfully.")
