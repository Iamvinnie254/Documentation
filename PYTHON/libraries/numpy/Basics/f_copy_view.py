

import numpy as np

arr = np.array([1,2,3,4,5,6])
x = arr.copy()
y = arr.view()
arr[0] = 42

print(arr)
print(x)
print(y)

# checking if an array owns the data

print(x.base)
print(y.base)