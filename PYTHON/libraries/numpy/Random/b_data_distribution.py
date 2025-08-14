# Data distribution is a list of all possible values, and how often each value occurs
# probability density function is a function that describes a continuous probability i.e. probability of all values in an array.


from numpy import random

x = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(100))
x2 = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(3,5))

print(x)
print(x2)