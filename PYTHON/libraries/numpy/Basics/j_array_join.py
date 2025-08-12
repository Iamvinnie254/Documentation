# Putting contents of two or more arrays in a single array
# we use axes to join arrays in numpy

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1, arr2))
arrx = np.stack((arr1, arr2), axis=1)
arrrow = np.hstack((arr1, arr2)) # stacking along rows
arrY = np.vstack((arr1, arr2)) # stacking along columns
print(arr)
print(arrx)
print(arrrow)
print(arrY)