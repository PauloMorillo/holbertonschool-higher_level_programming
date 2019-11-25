-- this script list all records
-- list all with exist name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
