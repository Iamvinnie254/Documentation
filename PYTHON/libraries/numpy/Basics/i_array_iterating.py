# Iterating means going through an element one by one

import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

for a in arr:
    print(a)

for x in arr:
    for a in x:
        print(a)

for y in arr:
    for x in y:
        for a in x:
            print(a)


##### This iterates through each scalar .

for  x in np.nditer(arr):
    print(x)


# different datatypes

for a in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(a)


# using different step size

for a in np.nditer(arr[:, ::2]):
    print(a)

# Enumerated iterating
for idx, x in np.ndenumerate(arr):
    print(idx, x)