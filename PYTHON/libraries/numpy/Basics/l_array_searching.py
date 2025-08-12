# 

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

x = np.where(arr == 4)
y = np.where(arr%2 == 0) # even indexes
y2 = np.where(arr%2 == 1) # odd indexes
z = np.searchsorted(arr, 7, side='right') # search sorted
print(x)
print(y)
print(y2)
print(z)