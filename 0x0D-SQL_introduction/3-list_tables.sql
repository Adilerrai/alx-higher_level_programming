-- printing all tables of DB 
CREATE PROCEDURE list_tables(database_name VARCHAR(255))
BEGIN
	  SELECT table_name
	  FROM information_schema.tables
	  WHERE table_schema = database_name;
END;

CALL list_tables('database_name');
