import os
import cx_Oracle
import csv
import pandas as pd

# create connection to Oracle
conn = cx_Oracle.connect(user="c##MASTER_SCHEMA", password="d33p", dsn="localhost/deep", encoding="UTF-8")

# run SQL query

sql_query = pd.read_sql_query('''select * from EMP where WORK_LOC like '%KOL%' ''', conn)

# Write the dataframe in to a CSV file

sql_query.to_csv(r'EMP_data_orcl.csv', index=False)

newsql_query = pd.read_sql_query('''select * from EMP where WORK_LOC like '%DEL%' ''', conn)

newsql_query.to_csv('EMP_data_orcl.csv', mode='a', header=False, index=False)
