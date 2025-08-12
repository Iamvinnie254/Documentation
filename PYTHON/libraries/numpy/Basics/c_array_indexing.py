# Array indexing is the same as accesing an array element

import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr[3])
print(arr[2]+arr[4])

# 2-D array

arr = np.array([[1,2,3],[4,5,6]])
print("Second element on first row: ",arr[0,1])

# 3-D array
arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr[0,1,2])