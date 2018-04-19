# Claire Drummond April-19-2018
# Key Statistics of the Iris Data Set using Pandas 
# Ref: https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/


# Load libraries to enable data plotting on graphs
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load dataset from UCI Machine Learning repository
iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'] #Give each column a named heading
dataset = pandas.read_csv(iris_url, names=names)

# box plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# histograms - alternative method to code in mean.py
dataset.hist()
plt.show()

#scatter plot matrix
scatter_matrix(dataset)
plt.show()