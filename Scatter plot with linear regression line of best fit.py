# If you want to understand how two variables change with respect to each other,
# the line of best fit is the way to go.
# The below plot shows how the line of best fit differs amongst various groups in the data.
# To disable the groupings and to just draw one line-of-best-fit for the entire dataset, remove the hue='cyl' parameter from the sns.lmplot() call below.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.simplefilter('ignore')

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4, 8]), :]

# Plot
sns.set_style("white")
# gridobj = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select,
#                      height=7, aspect=1.6, robust=True, palette='tab10',
#                      scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

gridobj = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select,
                     aspect=1.6, robust=True, palette='tab10',
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))


# Decorations
gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=20)
plt.show()
