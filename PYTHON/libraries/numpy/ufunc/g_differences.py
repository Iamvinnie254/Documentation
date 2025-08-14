

import numpy as np

arr = np.array([10,15,25,5])

newarr = np.diff(arr)
print(newarr)

x2 = np.diff(arr, n=2)
print(x2)