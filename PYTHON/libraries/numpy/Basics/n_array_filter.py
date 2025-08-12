# Filtering is getting some elements outt of an existing array and creating a new array out of them.
# in numpy we use boolean index

import numpy as np

arr= np.array([1,2,3,4])

x = [True, False, True, False]

newarr = arr[x]
print(newarr)

##########

filter_arr = []

for element in arr:
    if element > 2:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)