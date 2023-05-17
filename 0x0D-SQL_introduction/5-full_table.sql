-- Describe a table
USE hbtn_0c_0;

SELECT CONCAT('Table   Create Table') AS Description
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table'
UNION ALL
SELECT CONCAT(table_name, '     ', create_statement)
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';

