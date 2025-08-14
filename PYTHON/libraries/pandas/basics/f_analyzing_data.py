# The head() method returns the headers and a specified number of rows, starting from the top


import pandas as pd

df = pd.read_csv('data.csv')
print(df.head(10))
print(df.head())
print(df.tail())
print(df.info())