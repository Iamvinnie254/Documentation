# Optimizers are a set of procedures defined in scipy that either find the minimum value of a function, or the root of an equation

from scipy.optimize import root, minimize
from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)
print(myroot.x)
print(myroot)

def eqn2(x2):
    return x2**2 + x2 + 2

mymin = minimize(eqn2, 0 , method='BFGS')
print(mymin)