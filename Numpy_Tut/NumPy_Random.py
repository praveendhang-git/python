import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Example: Plot a histogram of random numbers

# sns.displot([1, 2, 4, 5])

# plt.show()

# sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
# plt.show()
binmial = np.random.binomial(n=100, p=0.5, size=8)

sns.displot(binmial, kind="kde")

plt.show()
