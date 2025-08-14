# Pandas is a python library used for working with data sets
# Pandas is used to analyze data
# pandas has functions for analyzing, cleaning, exploring, and manipulating data.
# Pandas refers to both "panel data" and "python data analysis" and ws created by Wes McKinney in 2008

# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy datasets, and make them readable and relevant.


# Data sciemce is a branch of computer science where we study how to store, use and analuze data for deriving information from it.

# What can pandas do:
# Pandas gives you answers about the data. like:
# is there a correlation between two or more columns?
# what is the average value?
#max value?
# min value?
# PANDAS are able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.



import pandas


dataset = {
    'cars':['BMW','Volvo','Ford'],
    'passings': [3,7,2]
}

myvar = pandas.DataFrame(dataset)
print(myvar)
