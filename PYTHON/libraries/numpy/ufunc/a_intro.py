# ufuncs stands for "universal functions" and they are Numpy functions that operate on the ndarray object
# ufuncs are used to implement vectorization in numpy which is way faster than iterating elements
#Vectorization is converting iterative statements into a vector based operation.


import numpy as np
x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x,y)
print(z)


# creating your own ufunc(universal function)

def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd, 2,1)

print(myadd([1,2,3,4],[5,6,7,8]))
print(type(np.add))