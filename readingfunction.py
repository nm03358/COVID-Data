#readingfunction.py
#Nicholas Mourfield

import pandas as pd

#read = pd.read_csv(r'https://github.com/nm03358/COVID-Data/blob/National/all-states-history.csv', index_col=0)
read = pd.read_csv(r'file://localhost/Users/nich/Desktop/Capstone/Code/data/helpmeplz.csv', index_col=0)
df = read
print(df.head(5))