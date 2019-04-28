#Pairwise plot is a favorite in exploratory analysis to understand the relationship between all possible pairs of numeric variables.
# It is a must have tool for bivariate analysis.



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


# Load Dataset
df = sns.load_dataset('iris')

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="scatter", hue="species", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
plt.show()



# Load Dataset
df = sns.load_dataset('iris')

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="reg", hue="species")
plt.show()