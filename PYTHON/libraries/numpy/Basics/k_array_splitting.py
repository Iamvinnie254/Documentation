# Splitting is the reverse process of joining

import numpy as np

arr  = np.array([1,2,3,4,5,6,7,8,9])

newarr = np.array_split(arr, 3)
newarr2 = np.array_split(arr, 4)
print(newarr)
print(newarr2)