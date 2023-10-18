-- creating list without join
USE hbtn_0d_usa;

-- Find the state_id for California
SELECT id INTO @california_id FROM states WHERE name = 'California';

-- List all the cities of California
SELECT id, name
FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;
