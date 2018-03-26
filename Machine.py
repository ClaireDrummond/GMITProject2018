# Claire Drummond 2018-03-26
# ref: http://www.scipy-lectures.org/packages/scikit-learn/

# scikit-learn embeds a copy of the iris CSV file along with a function to load it into numpy arrays 
from sklearn.datasets import load_iris
iris = load_iris()

#The features of each sample flower are stored in the data attribute of the dataset
print(iris.data.shape)

n_samples, n_features = iris.data.shape
print(n_samples)

print(n_features)


print(iris.target_names) #The names of the classes are stored in the last attribute, namely target_names

# The information about the class of each sample is stored in the target attribute of the dataset
print(iris.target.shape)

print(iris.target)

