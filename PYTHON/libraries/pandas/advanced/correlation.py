# The corr() method calculates the relationship between each column in your dataset.

import pandas as pd


df = pd.read_csv('data.csv')

print(df.corr())