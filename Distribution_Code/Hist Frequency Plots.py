import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

data = [1000, 1000, 5000, 3000, 4000, 16000, 2000]

plt.hist(data, weights=np.ones(len(data)) / len(data))

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
