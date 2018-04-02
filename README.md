## Project2018-IrisDataSet
Programming and Scripting Data Analytics Project 2018

# Introduction
A dataset is a collection of data.  It corressponds to the contents of a single database table. Every column of the table represents a particular variable, and each row corresponds to a given member of the data set in question. The data set lists values for each of the variables, such as height and weight of an object, for each member of the data set.  The Iris dataset has been used extensively in statistical literature.  Right now, at 21:23 on Sunday March 25th, I have no idea why.......so here goes, lets investigate!

# Why Iris Data Set?
According to Wikipedia 'The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"'

This doesn't help me much to be honest.  Lets try and find out more about the Iris Data Set in layman's terms:
The data set contains 150 records of three different types (classes) of iris flowers with numeric values for petal length and width and sepal length and width.  This data set is traditionally used for classification and prediction – to see which features of an iris can identify the flower as a certain type of iris. The values for length and width can be used to classify an iris into one of three iris types: Iris setosa, Iris versicolor, or Iris virginica. Visually exploring this data also lets you see the grouping (clustering) of the records into these three different types of irises (ref: https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-the-iris-data-set/).

So it appears that the reason the Iris Data Set is used so much in Data Analytics is because the data set is a classic, well-known data set example for data mining and data exploration. 

# Back to Basic with the Python Tutorial
Before I jump on in to Machine Learning and importing libraries to Python to help me manipulate the data, I think it is best to explore the basics of reading files in Python

# Machine Learning
After a few hours of research, scroling through websites and watching YouTube videos, it is apparent that Data Scientists love Python and most scientists in the industry use a combination of numpy + pandas + sklearn as their data science stack.  Having a brief look of what sklearn can do, I have created a file Machine.py to import sklearn and try out some code.

# Summary of Files
Data/Iris.csv: Iris Data Set File imported as CSV file
Format.py: Python Code that formats the Iris Data Set
Tutorial.py: Applying the learnings in https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files and using them on the Iris Data Set
Machine.py: Import sklearn and try some code

# References Used
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-the-iris-data-set/
http://www.scipy-lectures.org/packages/scikit-learn/
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
