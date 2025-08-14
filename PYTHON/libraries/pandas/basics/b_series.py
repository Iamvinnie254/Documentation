# A pandas series is like a column in a table
#It is a 1-D array holding data of any type


import pandas as pd

a = [1,7,2]

myvar = pd.Series(a)
print(myvar)


#LABELS
# If nothing else is specified, the values are labeled with their index number.

print(myvar[0])


#Creating Labels
myvar2 = pd.Series(a, index=["x","y","z"])
print(myvar2)



# Key value objects as series

calories = {'day1':420,'day2':380,'day3':390}

cals = pd.Series(calories)
cals2 = pd.Series(calories, index=['day1','day2'])
print(cals)
print(cals2)


### DataFrames 
# Data sets in pandas are usually multidimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table

data = {
    'calories': [420,380,390],
    'duration': [50,45,40]
}

cals3 = pd.DataFrame(data)
print(cals3)