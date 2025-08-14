# It is a discrete distribution
# It estimates how many times an event can happen in a specified time e.g. if someone eats twice a day what is the pribability that he will eat twice?
# It has two parameters:

# lam - rate or known number of occurences e.g. 2 for above problem
# size - The shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns




x = random.poisson(lam=2, size=10)
print(x)

sns.displot(random.poisson(lam=2, size=1000))
plt.show()

# difference between normal and poisson distribution

data = {
    "normal": random.normal(loc=50, scale=7, size=1000),
    "poisson": random.poisson(lam=50, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

# difference between poisson distribution and binomial distribution

data={
    "binomial": random.binomial(n=1000, p=0.01, size=1000),
    "poisson": random.poisson(lam=10, size=1000)
}
sns.displot(data, kind="kde")
plt.show()