import pandas 



# Load dataset from UCI Machine Learning repository

iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

dataset = pandas.read_csv(iris_url, names=names)



# shape

print(dataset.shape)



# head

print(dataset.head(10))



# descriptions

print(dataset.describe())






    