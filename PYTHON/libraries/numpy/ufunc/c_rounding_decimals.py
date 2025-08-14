# truncation, fix, rounding, floor, ceil

import numpy as np


arr = np.trunc([-3.6668,3.7774])
print(arr)
arr2 = np.fix([-3.6668,3.7774])
print(arr2)

arr3  = np.round(3.1235,2)
print(arr3)
arr4 = np.floor([-3.6668,3.7774])
print(arr4)
arr5 = np.ceil([-3.6668,3.7774])
print(arr5)