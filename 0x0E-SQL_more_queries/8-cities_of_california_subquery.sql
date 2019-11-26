-- Script that select for a realtional database
-- select cities from states
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
