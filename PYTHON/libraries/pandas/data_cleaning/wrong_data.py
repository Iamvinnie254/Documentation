

import pandas as pd

df = pd.read_csv('data.csv')

for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x,'Duration'] = 120

print(df.to_string())


# removing rows

for x in df.index:
    if df.loc[x, 'Duration'] == 120:
        df.drop(x, inplace=True)

print(df.to_string())