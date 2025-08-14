# The normal or Gaussian distribution 

# Has three parameters:
# loc - (Mean) where the peak of the bell exists
# scale - (standard deviation) how flat the graph distribution should be.
# size - The shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.normal(size=(2,3))
x2  = random.normal(loc=1, scale=2, size=(2,3))
print(x)
print(x2)

sns.displot(random.normal(size=1000), kind="kde")
plt.show()