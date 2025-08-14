# A distribution following Pareto's law i.e.80-20 distribution (20% factors cause 80% outcome)
# it has 2 parameters:
# a - shape parameter
# size - Shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.pareto(a=2, size=(2,3))
print(x)

sns.displot(random.pareto(a=2,size=1000), kind='kde')
plt.show()