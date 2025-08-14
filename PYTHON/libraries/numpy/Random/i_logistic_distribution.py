# This is used to describe growth
# Used extensively in machine learning in liistic regression, neural networks etc.

# It has three parameters:
# loc - mean, where peak is default 0
# scale - standard deviation, the flatness of distribution Default = 1
# size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.logistic(loc=1, scale=2, size=(2,3))
print(x)


sns.displot(random.logistic(size=1000), kind="kde")
plt.show()

# difference between logistic and normal distribution
data = {
    "normal": random.normal(scale=2, size=1000),
    "logistic": random.logistic(size=1000)
}
sns.displot(data, kind='kde')
plt.show()