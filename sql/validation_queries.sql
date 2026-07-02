-- ================================
-- 1. Missing Values
-- ================================
SELECT *
FROM parts
WHERE manufacturer IS NULL
   OR model IS NULL
   OR category IS NULL
   OR part_name IS NULL
   OR price IS NULL;

-- ================================
-- 2. Duplicate Records
-- ================================
SELECT manufacturer, model, part_name, price, COUNT(*) AS duplicate_count
FROM parts
GROUP BY manufacturer, model, part_name, price
HAVING COUNT(*) > 1;

-- ================================
-- 3. Invalid Prices
-- ================================
SELECT *
FROM parts
WHERE price <= 0
   OR price IS NULL;

-- ================================
-- 4. Brand Statistics
-- ================================
SELECT manufacturer, COUNT(*) AS total_parts
FROM parts
GROUP BY manufacturer
ORDER BY total_parts DESC;

-- ================================
-- 5. Category Statistics
-- ================================
SELECT category, COUNT(*) AS total_parts
FROM parts
GROUP BY category
ORDER BY total_parts DESC;

-- ================================
-- 6. Price Distribution
-- ================================
SELECT
    CASE
        WHEN price < 50 THEN 'Low (0–50)'
        WHEN price BETWEEN 50 AND 150 THEN 'Medium (50–150)'
        WHEN price > 150 THEN 'High (150+)'
    END AS price_range,
    COUNT(*) AS total_parts
FROM parts
WHERE price IS NOT NULL
GROUP BY price_range
ORDER BY total_parts DESC;

-- ================================
-- 7. Potential AI Duplicate Candidates
-- (similar names, not exact duplicates)
-- ================================
SELECT p1.part_id AS id1,
       p1.part_name AS name1,
       p2.part_id AS id2,
       p2.part_name AS name2
FROM parts p1
JOIN parts p2
  ON p1.part_id <> p2.part_id
 AND p1.part_name ILIKE '%' || SPLIT_PART(p2.part_name, ' ', 1) || '%'
LIMIT 50;
