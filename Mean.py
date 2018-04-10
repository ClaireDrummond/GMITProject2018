# Claire Drummond 2018-04-10
# Iris Data Set Analysis
# Ref: Programming and Scripting Week 10 Videos

# Calculate the mean of each Column
import numpy

# Read data file into array
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
# picking the first column of data
firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0]) #defining meanfirstcol
print("Mean of First Column is:", meanfirstcol)

# picking the second column of data
secondcol = data[:,1]
meansecondcol = numpy.mean(data[:,1]) #defining meansecondcol
print("Mean of Second Column is:", meansecondcol)

# picking the third column of data
thirdcol = data[:,2]
meanthirdcol = numpy.mean(data[:,2]) #defining meanthirdcol
print("Mean of Third Column is:", meanthirdcol)

# picking the forth column of data
forthcol = data[:,3]
meanforthcol = numpy.mean(data[:,3]) #defining meanforthcol
print("Mean of Forth Column is:", meanforthcol)

# Importing MatplotLib to enable plotting of Histogram
import matplotlib.pyplot as pl 
pl.hist(firstcol)
pl.show()




