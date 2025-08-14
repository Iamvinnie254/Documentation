# It is used fr describing time till next event e.g failure/success
# it has 2 parameters:
# scale - inverse of rate
# size - The shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.exponential(scale=2, size=(2,3))

print(x)

sns.displot(random.exponential(size=1000), kind='kde')
plt.show()



# poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events