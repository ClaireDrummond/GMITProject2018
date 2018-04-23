

import seaborn as sns
df = sns.load_dataset('iris')

df.groupby('species').mean()
print (df.groupby('species').mean())



import pandas as pd
df = pd.read_csv( 'data/iris.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'] )
df.groupby('species').mean()
print (df.groupby('species').mean())

import pandas as pd
df = pd.read_csv( 'data/iris.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'] )
df.groupby('species').median()
print (df.groupby('species').median())





