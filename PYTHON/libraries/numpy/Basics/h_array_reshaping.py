# chanaging the shape of an array
# shape of an array is the number of elements in each dimension


import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8,9])

newarr = arr.reshape(3,3)

print(newarr)
print(newarr.base)

# flattening an array is converting a multidimensiional one to a 1-d array


arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
newarr2 = arr.reshape(-1)

print(newarr2)