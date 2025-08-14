# Either you remove the rows or convert all cells in the columns into the same format

import pandas as pd


df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())

##removing rows

df.dropna(subset=['Date'], inplace=True)