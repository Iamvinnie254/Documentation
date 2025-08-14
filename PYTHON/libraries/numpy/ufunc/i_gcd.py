import numpy as np

num1 = 2
num2 = 4
arr = np.array([1,2,3,4])

x = np.gcd(num1,num2)
x2 = np.gcd.reduce(arr)

print(x)
print(x2)