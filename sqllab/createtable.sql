DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time with time zone,
  latitude real,
  id text,
  place text,
  type text,
  locationSource text

);