-- task_6.sql

USE alx_book_store;

SET @sql = CONCAT(
    'INSERT INTO ', 'customer', ' ',
    'SELECT 2, ''Blessing Malik'', ''bmalik@sandtech.com'', ''124 Happiness  Ave.'' UNION ALL ',
    'SELECT 3, ''Obed Ehoneah'', ''eobed@sandtech.com'', ''125 Happiness  Ave.'' UNION ALL ',
    'SELECT 4, ''Nehemial Kamolu'', ''nkamolu@sandtech.com'', ''126 Happiness  Ave.'''
);

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
