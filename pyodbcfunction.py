#pyodbcfunction.py
#Nicholas Mourfield

import pyodbc
import pandas as pd

databaseName = 'covid-project-db'
username = 'NMourfield'
password = 'Pa$$word'
server = 'covid-project-server.database.windows.net'
driver= '{ODBC Driver 17 for SQL Server}'
CONNECTION_STRING = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+databaseName+';UID='+username+';PWD='+password

conn = pyodbc.connect(CONNECTION_STRING)
cursor = conn.cursor()