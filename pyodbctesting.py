#Nicholas Mourfield

import pyodbc
import pandas as pd
import sqlalchemy

databaseName = 'covid-project-db'
username = 'NMourfield'
password = 'Pa$$word'
server = 'covid-project-server.database.windows.net'
driver= '{ODBC Driver 17 for SQL Server}'
CONNECTION_STRING = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+databaseName+';UID='+username+';PWD='+password

conn = pyodbc.connect(CONNECTION_STRING)
cursor = conn.cursor()

statenames = open(r"c:/Users/nm03358\Documents/Capstone/txtfiles/statenames.txt")
lines = statenames.readlines()
count = 0
urllist = []
for i in lines:
    i = i.rstrip()
    url = ("https://raw.githubusercontent.com/nm03358/COVID-Data/States/"+i+"-history.csv")
    urllist.append(url)

for url in urllist:
    read = pd.read_csv(url, index_col=0)
    df = read
    print(df)

conn.close()
