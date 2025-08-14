# This is done by removing the rows that conatain the empty cells.


import pandas as pd

df = pd.read_csv('data.csv')
new_df = df.dropna() # does not change the original dataframe but returns a new one
#new_df2 = df.dropna(inplace=True) # Will not return a new dataframe but will remove all rows conatining NULL values from the original dataframe

print(new_df.to_string())
#print(new_df2)

df.fillna(130, inplace=True)