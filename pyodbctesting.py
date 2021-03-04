#Nicholas Mourfield

import pyodbc
import pandas as pd
import sqlalchemy
from sqlalchemy import Table, MetaData, Column, Integer
import urllib

databaseName = 'covid-project-db'
username = 'NMourfield'
password = 'Pa$$word'
server = 'covid-project-server.database.windows.net'
driver= '{ODBC Driver 17 for SQL Server}'
CONNECTION_STRING = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+databaseName+';UID='+username+';PWD='+password

conn = pyodbc.connect(CONNECTION_STRING)
cursor = conn.cursor()

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 10.0};SERVER=covid-project-server.database.windows.net;DATABASE=covid-project-db;UID=NMourfield;PWD=Pa$$word")
engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

statenames = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new-hampshire', 'new-jersey', 'new-mexico', 'new-york', 'north-carolina', 'north-dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode-island', 'south-carolina', 'south-dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west-virginia', 'wisconsin', 'wyoming']
count = 0
urllist = []
tablenames = []
for i in statenames:
    i = i.rstrip()
    url = ("https://raw.githubusercontent.com/nm03358/COVID-Data/States/"+i+"-history.csv")
    urllist.append(url)
    tablenames.append(i)

datapass = {tablenames[i]: urllist[i] for i in range(len(tablenames))} 

for i in datapass:
    df = pd.read_csv(datapass[i], index_col=0)
    print(i)
    print(df.head(5))
    #df.to_sql(i, engine)

conn.close()
