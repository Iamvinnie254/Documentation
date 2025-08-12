# strings, integer, float, boolean, complex


import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
arr2 = np.array(['kiwi','mango','cherry'])

print(arr.dtype)
print(arr2.dtype)

# creating an array with a defined data type

arr = np.array([1,2,3,4], dtype='S')
print(arr)
print(arr.dtype)