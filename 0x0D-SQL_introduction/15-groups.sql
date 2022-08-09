-- List number of records with same score in the table.
-- Query that lists the number of records with the same score in the table.
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
