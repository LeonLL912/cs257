-- Find the earthquakes that have magnitude between 4 and 5
SELECT * FROM earthquakes WHERE mag BETWEEN 4 AND 5
liangl-> INTERSECT
-- Find the earthquakes that occurred in Alaska
liangl-> SELECT * FROM earthquakes WHERE longitude BETWEEN -180 AND -130 AND latitude BETWEEN 52 AND 71
liangl-> ORDER BY mag DESC;


-- Find the earthquakes that have magnitude from 3 to 5
liangl=> SELECT * FROM earthquakes WHERE mag BETWEEN 3 AND 5
liangl-> INTERSECT
-- Find the earthquakes that are in type earthquake
liangl-> SELECT * FROM earthquakes WHERE quaketype = 'earthquake'
liangl-> ORDER BY mag DESC;


-- Find the earthquakes that have longitude from 0 to 180 (East part of Earth? depending on how the author define negative sign in this csv file)
liangl=> SELECT * FROM earthquakes WHERE longitude BETWEEN 0 AND 180
liangl-> INTERSECT
-- Find the earthquakes that have latitude from 0 to 90 (North part of Earth? depending on how the author define negative sign in this csv file)
liangl-> SELECT * FROM earthquakes WHERE latitude BETWEEN 0 AND 90
liangl-> ORDER BY mag DESC;
