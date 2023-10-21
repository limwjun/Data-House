# sql-create-log
##Description
1. The goal of this project is to create an automated log to capture the status of MS SQL Server store procedures during batch processing.
2. There are 3 sql files with the following description:
   a.  sp_etl_create_logs - To create the store procedure that writes into the etl_msg_logs table
   b.  create_table_etl_logs - To create the etl_msg_logs table
   c.  sp_test - To create store procedure to test item a and b

##Steps
1.  Execute all three files using any SQL Server tool (I use VSCode on macos).
2.  Test it out yourself! In the following example, running the first execute statement should not show an error but the second execute statement will yield an error.

USE maindb

EXECUTE sp_test '20231003','N','SELECT ''a''';
EXECUTE sp_test '20231003','N','SELECT a';

SELECT * from etl_msg_logs;
