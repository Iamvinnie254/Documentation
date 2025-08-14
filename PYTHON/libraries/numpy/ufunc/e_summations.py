#

import numpy as np

arr = np.array([1,2.3])
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])

newarr = np.add(arr1, arr2)
newarr2 = np.sum([arr1, arr2])
newarr3 = np.cumsum(arr)

print(newarr)
print(newarr2)
print(newarr3)