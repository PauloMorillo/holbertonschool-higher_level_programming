-- this script list all records
-- list all with exist name
SELECT score, name FROM second_table WHERE EXISTS (SELECT name FROM second_table) ORDER BY score DESC;
