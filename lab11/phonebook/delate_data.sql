CREATE OR REPLACE PROCEDURE delate_data(data_to_delate VARCHAR(20))
	AS $$	
	BEGIN
	DELETE FROM tsis11 WHERE name = data_to_delate OR number = data_to_delate;
	END; $$
	LANGUAGE plpgsql