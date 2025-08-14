# Chi square distribution is used as a basis to verify the hypothesis

# It has 2 parameters:
# df - degree of freedom
# size - the shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.chisquare(df=2, size=(2,3))
print(x)

sns.displot(random.chisquare(size=1000, df=2), kind='kde')
plt.show()