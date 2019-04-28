#Often multiple datapoints have exactly the same X and Y values.
# As a result, multiple points get plotted over each other and hide.
# To avoid this, jitter the points slightly so you can visually see them.
# This is convenient to do using seaborn’s stripplot().

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")

# Draw Stripplot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
sns.stripplot(df.cty, df.hwy, jitter=0.25, size=8, ax=ax, linewidth=.5)

# Decorations
plt.title('Use jittered plots to avoid overlapping of points', fontsize=22)
plt.show()