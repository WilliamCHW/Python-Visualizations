# Another option to avoid the problem of points overlap is the increase the size of the dot depending on how many points lie in that spot.
# So, larger the size of the point more is the concentration of points around that.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings



# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')

# Draw Stripplot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
sns.stripplot(df_counts.cty, df_counts.hwy, size=df_counts.counts*2, ax=ax)

# Decorations
plt.title('Counts Plot - Size of circle is bigger as more points overlap', fontsize=22)
plt.show()
