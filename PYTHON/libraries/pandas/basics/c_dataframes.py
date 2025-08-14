# A pandas DataFrame is a 2D data structure like a 2D array, or a table with rows and columns

import pandas as pd


data = {
    'calories':[450,320,520],
    'duration':[40,50,45]

}

df = pd.DataFrame(data)
print(df)

###locate row

print(df.loc[0])
print(df.loc[[0,1]])

## named indexes

df2 = pd.DataFrame(data, index=['day1','day2','day3'])
print(df2)

