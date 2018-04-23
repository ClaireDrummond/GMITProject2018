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

#Ref:https://stackoverflow.com/questions/49970309/how-do-i-calculate-the-mean-of-each-species-of-the-iris-data-set-in-python
# I posted question on stackoverflow to find the below code
import pandas as pd 
df = pd.read_csv( 'data/iris.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'] )
df.groupby('species').mean() # Separates the data into the 3 different species, then calculates the mean
print (df.groupby('species').mean())

# Using the above code, adjusted to get Median of each Species
df.groupby('species').median() # Separates the data into the 3 different species, then calculates the median
print (df.groupby('species').median())

# Using the above code, adjusted to get Standard Deviation of each Species
df.groupby('species').std() # Separates the data into the 3 different species, then calculates the standard deviation
print (df.groupby('species').std())

# Using the above code, adjusted to get Maximum Value of each Species
df.groupby('species').max() # Separates the data into the 3 different species, then calculates the maximum value
print (df.groupby('species').max())

# Using the above code, adjusted to get Minimum Value of each Species
df.groupby('species').min() # Separates the data into the 3 different species, then calculates the minimum value
print (df.groupby('species').min())

    