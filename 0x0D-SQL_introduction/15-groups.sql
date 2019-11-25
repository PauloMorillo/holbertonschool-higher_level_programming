-- this script computes the score average of all records
-- score count in a label
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
