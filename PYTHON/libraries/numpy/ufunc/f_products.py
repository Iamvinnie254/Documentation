#

import numpy as np

arr = np.array([1,2,3])
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])


x = np.prod(arr)
x1 = np.prod([arr1, arr2])
x3 = np.prod([arr1, arr2], axis=1)
x4 = np.cumprod(arr)


print(x)
print(x1)
print(x3)
print(x4)