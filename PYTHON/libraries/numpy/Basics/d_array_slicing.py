# Slicing arrays means taking elements from one given index to another given index

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr[1:5])
print(arr[4:])
print(arr[:6])
print(arr[-3:-1])

# Using the step value

print(arr[1:5:2])