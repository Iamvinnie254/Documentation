# Seaborn is a library that uses Matplotliub underneath to plot graphs. It will be used to visualize distributions
# Displot stand for distribution plot, it takes as aan input array an dplots a curve corresponding to the distribution of points in the array.

import matplotlib.pyplot as plt
import seaborn as sns


sns.displot([0,1,2,3,4,5])
plt.show()

# plotting a displot without the histogram

sns.displot([0,1,2,3,4,5], kind="kde")
plt.show()