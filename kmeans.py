# Claire Drummond April-12-2018
# Ref: http://www.dummies.com/programming/big-data/data-science/how-to-visualize-the-clusters-in-a-k-means-unsupervised-learning-model/

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris #Loads the Iris Data Set from SKlearn
iris = load_iris()
pca = PCA(n_components=2).fit(iris.data) # As the data set is large, this applies dimensionality reduction algorithm, thus giving a smaller number, representative of the data 
pca_2d = pca.transform(iris.data)

import pylab as pl #plotting of Graphs
for i in range(0, pca_2d.shape[0]):
   if iris.target[i] == 0:
       c1 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='r',
    marker='+')
   elif iris.target[i] == 1:
       c2 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='g', marker='o')
   elif iris.target[i] == 2:
    c3 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='b',
    marker='*')
pl.legend([c1, c2, c3], ['Setosa', 'Versicolor', # Naming the Legend on the Graph
    'Virginica'])
pl.title('Iris dataset with 3 clusters and known outcomes')
pl.show() 

#This is a plot representing how the known outcomes of the Iris dataset should look like. It is what you would like the K-means clustering to achieve.


