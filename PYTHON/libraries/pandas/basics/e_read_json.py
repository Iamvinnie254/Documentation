# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

import pandas as pd

df = pd.read_json('data.json')
print(df)
print(df.to_string())