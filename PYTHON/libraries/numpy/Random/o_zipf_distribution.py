# zipf distributions are used to sample data based on zipf's law.
# Zipf's Law: In a collection, the nth common term is 1/n times of the most common term e.g. the 5th  most common word in English occurs nearly 1/5 times as often as the most common word.

# it has 2 parameters:
# a - distribution parameter
# size - shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=(2,3))
print(x)

x2 = random.zipf(a=2, size=1000)
sns.displot(x2[x2<10])
plt.show()