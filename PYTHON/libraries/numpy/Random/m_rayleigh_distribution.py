# Rayleigh distribution is used in signal processing
# it has 2 parameters:
# scale = (standard deviation) decides how flat the distribution will be - default 1.0
# size = The shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.rayleigh(scale=2, size=(2,3))
print(x)

sns.displot(random.rayleigh(size=1000), kind="kde")
plt.show()