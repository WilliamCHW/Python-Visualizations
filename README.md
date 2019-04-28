# Python-Visualizations
There are 50 Visualizations which can you to finish 7 different purposes of data analysis. 

一共有50组图，可以实现7种不同的数据分析的目的。

 ## 1. Correlation
 ### 1.1 Scatter plot（散点图）
   
   Scatteplot is a classic and fundamental plot used to study the relationship between two variables. If you have multiple groups in your data you may want to visualise each group in a different color. In matplotlib, you can conveniently do this using plt.scatterplot().
   
   散点图是用于研究两个变量之间关系的经典的和基本的图表。 如果数据中有多个组，则可能需要以不同颜色可视化每个组。 在 matplotlib 中，您可以使用 plt.scatterplot（） 方便地执行此操作。
   
   ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Scatter%20plot.png)
   Code (代码): [Scatter plot.py](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Scatter%20plot.py)
    
 ### 1.2 Bubble plot with Encircling （带边界的气泡图）
    
   Sometimes you want to show a group of points within a boundary to emphasize their importance. In this example, you get the records from the dataframe that should be encircled and pass it to the encircle() described in the code below.
    
   有时，您希望在边界内显示一组点以强调其重要性。 在这个例子中，你从数据框中获取记录，并用下面代码中描述的 encircle（） 来使边界显示出来。
   
   ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Bubble%20plot%20with%20Encircling.png)
   Code(代码)：[Bubble plot with Encircling.py](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Bubble%20plot%20with%20Encircling.py)
    
 ### 1.3 Regression plot （回归拟合）  
 #### 1.3.1 Scatter plot with line of best fit （带线性回归最佳拟合线的散点图）
   
   If you want to understand how two variables change with respect to each other, the line of best fit is the way to go. The below plot shows how the line of best fit differs amongst various groups in the data. To disable the groupings and to just draw one line-of-best-fit for the entire dataset, remove the hue='cyl' parameter from the sns.lmplot() call below.
   
   如果你想了解两个变量如何相互改变，那么最佳拟合线就是常用的方法。 下图显示了数据中各组之间最佳拟合线的差异。 要禁用分组并仅为整个数据集绘制一条最佳拟合线，请从下面的 sns.lmplot（）调用中删除 hue ='cyl'参数。
 
 ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Scatter%20plot%20with%20line%20of%20best%20fit.png)
 Code(代码)：[Scatter plot with line of best fit.py](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Scatter%20plot%20with%20linear%20regression%20line%20of%20best%20fit.py)
 #### 1.3.2 Each regression line in its own column（针对每列绘制线性回归线）
 
   Alternately, you can show the best fit line for each group in its own column. You cando this by setting the col=groupingcolumn parameter inside the sns.lmplot().
   
   或者，可以在其每列中显示每个组的最佳拟合线。 可以通过在 sns.lmplot() 中设置 col=groupingcolumn 参数来实现。
   
 ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Each%20regression%20line%20in%20its%20own%20column.png)
 Code(代码)：[Each regression line in its own column.py](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Each%20regression%20line%20in%20its%20own%20column.py)
 ### 1.4 Jittering with stripplot （抖动图）
   
   Often multiple datapoints have exactly the same X and Y values. As a result, multiple points get plotted over each other and hide. To avoid this, jitter the points slightly so you can visually see them. This is convenient to do using seaborn’s stripplot().
 
   通常，多个数据点具有完全相同的 X 和 Y 值。 结果，多个点绘制会重叠并隐藏。 为避免这种情况，请将数据点稍微抖动，以便您可以直观地看到它们。 使用 seaborn 的 stripplot（） 很方便实现这个功能。
 
 ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Jittering%20with%20stripplot.png)
 Code(代码)：[Jittering with stripplot](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Jittering%20with%20stripplot.py)
 
 ### 1.5 Counts Plot（计数图）
 
   Another option to avoid the problem of points overlap is the increase the size of the dot depending on how many points lie in that spot. So, larger the size of the point more is the concentration of points around that.
 
   避免点重叠问题的另一个选择是增加点的大小，这取决于该点中有多少点。 因此，点的大小越大，其周围的点的集中度越高。
    
   ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Counts%20Plot.png)
 Code(代码)：[Counts Plot.py](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Counts%20Plot.py)
 ### 1.6 Marginal Histogram（边缘直方图）
 
   Marginal histograms have a histogram along the X and Y axis variables. This is used to visualize the relationship between the X and Y along with the univariate distribution of the X and the Y individually. This plot if often used in exploratory data analysis (EDA).
   
   边缘直方图具有沿 X 和 Y 轴变量的直方图。 这用于可视化 X 和 Y 之间的关系以及单独的 X 和 Y 的单变量分布。 这种图经常用于探索性数据分析（EDA）。
   
 ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Marginal%20Histogram.png)
 Code(代码)：[Marginal Histogram.py](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Marginal%20Histogram.py)
 ### 1.7 Marginal Boxplot（边缘箱形图）
 
   Marginal boxplot serves a similar purpose as marginal histogram. However, the boxplot helps to pinpoint the median, 25th and 75th percentiles of the X and the Y.
   
   边缘箱图与边缘直方图具有相似的用途。 然而，箱线图有助于精确定位 X 和 Y 的中位数、第25和第75百分位数。
   
   ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Marginal%20Boxplot.png)
   Code (代码):[Marginal Boxplot.py](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Marginal%20Boxplot.py)
 
 ### 1.8 Correlogram（相关图）
   
   Correlogram is used to visually see the correlation metric between all possible pairs of numeric variables in a given dataframe (or 2D array).
   
   相关图用于直观地查看给定数据框（或二维数组）中所有可能的数值变量对之间的相关度量。
  
  ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Correlogram.png)
 Code(代码)：[Correlogram.py](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Correllogram.py)
 ### 1.9 Pairwise Plot（矩阵图）
 
   Pairwise plot is a favorite in exploratory analysis to understand the relationship between all possible pairs of numeric variables. It is a must have tool for bivariate analysis.
   
   矩阵图是探索性分析中的最爱，用于理解所有可能的数值变量对之间的关系。 它是双变量分析的必备工具。
  
  ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Pairwise%20Plot.png)
  ![](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Image/Pairwise%20Plot2.png)
 Code(代码)：[Pairwise Plot.py](https://github.com/WilliamCHW/Python-Visualizations/blob/master/Correlation_Code/Pairwise%20Plot.py)
 
 ## 2. Deviation（偏差）
 ### 2.1 Diverging Bars（发散型条形图）
 
   If you want to see how the items are varying based on a single metric and visualize the order and amount of this variance, the diverging bars is a great tool. It helps to quickly differentiate the performance of groups in your data and is quite intuitive and instantly conveys the point.
   
   如果您想根据单个指标查看项目的变化情况，并可视化此差异的顺序和数量，那么散型条形图 （Diverging Bars） 是一个很好的工具。 它有助于快速区分数据中组的性能，并且非常直观，并且可以立即传达这一点。
   
  ![]()
  Code (代码): []()
  
 ### 2.2 Diverging Texts（发散型文本）
   
   Diverging texts is similar to diverging bars and it preferred if you want to show the value of each items within the chart in a nice and presentable way.
 
   发散型文本 （Diverging Texts）与发散型条形图 （Diverging Bars）相似，如果你想以一种漂亮和可呈现的方式显示图表中每个项目的价值，就可以使用这种方法。
  ![]()
  Code (代码): []()
 ### 2.3 Diverging Dot Plot（发散型包点图）
 
   Divering dot plot is also similar to the diverging bars. However compared to diverging bars, the absence of bars reduces the amount of contrast and disparity between the groups.
 
   发散型包点图 （Diverging Dot Plot）也类似于发散型条形图 （Diverging Bars）。 然而，与发散型条形图 （Diverging Bars）相比，条的缺失减少了组之间的对比度和差异。
  ![]()
  Code (代码): []()
 ### 2.4 Diverging Lollipop Chart with Markers（带标记的发散型棒棒糖图）
 
   Lollipop with markers provides a flexible way of visualizing the divergence by laying emphasis on any significant datapoints you want to bring attention to and give reasoning within the chart appropriately.
 
   带标记的棒棒糖图通过强调您想要引起注意的任何重要数据点并在图表中适当地给出推理，提供了一种对差异进行可视化的灵活方式。
  ![]()
  Code (代码): []()
 ### 2.5 Area Chart（面积图）
 
   By coloring the area between the axis and the lines, the area chart throws more emphasis not just on the peaks and troughs but also the duration of the highs and lows. The longer the duration of the highs, the larger is the area under the line.

   通过对轴和线之间的区域进行着色，面积图不仅强调峰和谷，而且还强调高点和低点的持续时间。 高点持续时间越长，线下面积越大。
  ![]()
  Code (代码): []()
