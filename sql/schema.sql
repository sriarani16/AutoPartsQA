CREATE TABLE IF NOT EXISTS parts (
    part_id        INTEGER PRIMARY KEY,
    manufacturer   VARCHAR(100),
    model          VARCHAR(100),
    category       VARCHAR(100),
    part_name      VARCHAR(200),
    price          NUMERIC
);

-- Optional table for cleaned data (if you want a single canonical table)
CREATE TABLE IF NOT EXISTS parts_cleaned (
    part_id        INTEGER,
    manufacturer   VARCHAR(100),
    model          VARCHAR(100),
    category       VARCHAR(100),
    part_name      VARCHAR(200),
    price          NUMERIC
);
