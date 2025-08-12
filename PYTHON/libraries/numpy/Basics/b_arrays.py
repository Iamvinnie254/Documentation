# The array object in numpy is called ndarray

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
print(type(arr))


# Dimensions in arrays id one level of array depth(nested arrays)

#0-D arrays
# These are the elements in an array (scalars)

arr = np.array(45)
print(arr)

# 1-D arrays
# An array that has 0-D arrays as its elements

arr =np.array([1,2,3,4,5])
print(arr)

# 2-D arrays
# An array that has 1-D arrays as its elements
# Used to oftenly represent matrices or 2nd order tensors

arr = np.array([[1,2,3],[4,5,6]])
print(arr)

#3-D arrays
# An array with 2-D arrays as its elements

arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)


# Checking number of dimensions

a = np.array(42)
b = np.array([1,2,3,4,5])

print(a.ndim)
print(b.ndim)

# Higher dimension arrays

arr = np.array([1,2,3,4,5,6], ndmin=5)
print(arr)
print('number of dimensions: ', arr.ndim)