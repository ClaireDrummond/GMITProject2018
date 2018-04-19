# Claire Drummond April-13-2018
# https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
# Scatterplot that shows the ratio between the width & length of Sepal Leafs & Petal Leafs

import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris")
iris["ID"] = iris.index
iris["ratio"] = iris["sepal_length"]/iris["sepal_width"] # Sepal Length and Width

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False)

plt.legend()
plt.show()


iris["ratio"] = iris["petal_length"]/iris["petal_width"] # Petal Length and Width

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False)

plt.legend()
plt.show()