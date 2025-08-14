import numpy as np

arr = np.array([3,6,9])
arr2 = np.arange(1,11)

x = np.lcm.reduce(arr)
x2 = np.lcm.reduce(arr2)

print(x)
print(x2)