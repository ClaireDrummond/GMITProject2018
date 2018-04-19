# Claire Drummond April-19-2018
# Key Statistics of the Iris Data Set using Pandas 
# Ref: https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/

import pandas # library for statistics in data anaylsis

# Load dataset from UCI Machine Learning repository - new learning

iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

dataset = pandas.read_csv(iris_url, names=names)



# shape - this tells quantity of rows and columns in the dataset
print(dataset.shape)

# head - prints first ten rows of the dataset
print(dataset.head(10))

# description - prints keys stats on the dataset
print(dataset.describe())






    