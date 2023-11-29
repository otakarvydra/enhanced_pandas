## Enhanced Pandas

This script includes various functions to clean/validate a dirty .csv file to make the life of data analysts/scientists easier

Some of these functions simply check if there is a distinct data type present in a column. This is because data types in pandas are inferred and not enforced. Therefore if there is one numeric value in a column full of strings, the overall datatype of the column will be object. 

The included functions are: 

1 - viewna_all - views the sum of missing values as well as the percentage of missing values for each column in a dataframe

2 - viewna_column - groups the sum of missing values in a column by unique values of a different column. Is useful for determining what is the cause of the missing data

3 - check_missing_time_records - loops through column that includes timestamps of given format and checks if there are any missing records

4 - normalize - creates a normalized table with a primary key column from a base table

5 - check_bool - checks for boolean values inside of a column

6 - check_numeric - checks for numeric values inside of a column

7 - check_empty_values - checks if there are strings usually used to denote missing values in a column ('empty, unknown' etc.)

8 - sort_check - sorts column and provides n first and n last values. Any unorthodox elements will either float to the top or bottom

9 - check_headers - checks if there are headers in any of the columns of a given dataframe