-- Script that select all cities in the database
-- select cities from states
SELECT cities.id, cities.name, states.name FROM states INNER JOIN cities ON states.id = cities.state_id;
