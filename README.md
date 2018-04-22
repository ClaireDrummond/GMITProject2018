
# Project2018-IrisDataSet
Programming and Scripting Data Analytics Project 2018

# Introduction
A dataset is a collection of data.  It corresponds to the contents of a single database table. Every column of the table represents a particular variable, and each row corresponds to a given member of the data set in question. The data set lists values for each of the variables, such as height and weight of an object, for each member of the data set.  The Iris dataset has been used extensively in statistical literature.  Right now, at 21:23 on Sunday March 25th, I have no idea why.......so here goes, lets investigate!

# Why Iris Data Set?
It appears that the reason the Iris Data Set is used so much in Data Analytics is because the data set is a classic, well-known data set example for data mining and data exploration. According to Wikipedia 'The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"'

This doesn't help me much to be honest.  Lets try and find out more about the Iris Data Set in layman's terms:
The data set contains 150 records of three different types (classes) of iris flowers with numeric values for petal length and width and sepal length and width.  This data set is traditionally used for classification and prediction – to see which features of an iris can identify the flower as a certain type of iris. The values for length and width can be used to classify an iris into one of three iris types: Iris setosa, Iris versicolor, or Iris virginica. Visually exploring this data also lets you see the grouping (clustering) of the records into these three different types of irises (ref: https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-the-iris-data-set/).

The purpose of a discriminant analysis is to produce a simple function that, given the four measurements, will classify a flower correctly. This is the beginning of creating “predictors” in order to try to make a more educated guess on a record in a dataset. I will attempt to analyze this dataset to try to draw some conclusions. 
 
# Back to Basics with the Python Tutorial
## CSVModule.py and Tutorial.py
Before I jump on in to Machine Learning and importing libraries to Python to help me manipulate the data, I think it is best to explore the basics of reading files in Python. In the file CSVModule.py, I am importing the CSV module to manipulate the Iris Data File. To pull information from CSV files you use loop and split methods to get the data from individual columns.The CSV module explicitly exists to handle this task, making it much easier to deal with CSV formatted files. This becomes especially important when you are working with data that’s been exported from actual spreadsheets and databases to text files. In Tutorial.py, I am using code to view certain parts of the dataset and learn more about its contents.   

# Exploring Python Libraries 
## Machine.py
After a few hours of research, scrolling through websites and watching YouTube videos, it is apparent that Data Scientists love Python and most scientists in the industry use a combination of numpy + pandas + sklearn as their data science stack. In Machine.py I use SKlearn to help me capture detail on the Iris Data Set
 
# Statistics
## Stats.py
The Pandas Library is ideal for statisitcal analyis in datasets. Using the command 'describe', pandas has helped me identitfy key statstical infomartion on the data set.

# Visualising the Data
## Mean.py, Graphs.py, Scatterplot.py, Seaborn.py
In week 10, of Programming and Scripting Module, I was introduced to Numpy which is ideal for data anaylsis.  Here I have created code to establish the mean of each column.  To understand each column in more detail, I have created histograms.  In the file Graphs.py, I have used pandas and matplot to plot the data onto graphs, box plots, histograms, scattermatrix. Scatterplot.py uses code that colourcodes the different Iris flowers, thus showing a more impactful scatterplot than the one created in Graphys.py.
Using Seaborn I have created a scatterplot that shows the ratio between the width & length of the Sepal leaf and the Petal Leaf
https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
All graphs are uploaded to the repository.

#Key Findings
Currently working on word doc to upload to git hub


# Summary of Files
Data/Iris.csv
Tutorial.py
Csvmodule.py
Machine.py
Graphs.py
Mean.py
Seaborn.py
Scatterplot.py
Stats.py

# References Used
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-the-iris-data-set/
http://www.scipy-lectures.org/packages/scikit-learn/
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
http://www.dummies.com/programming/big-data/data-science/how-to-visualize-the-clusters-in-a-k-means-unsupervised-learning-model/
http://stamfordresearch.com/k-means-clustering-in-python/
https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
https://pandas.pydata.org/
https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/
http://seaborn.pydata.org/tutorial/distributions.html
