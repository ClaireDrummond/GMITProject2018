
# Calculate the mean of each Column
import numpy

# Read data file into array
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
# picking the first column of data
firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
forthcol = data[:,3]

meanfirstcol = numpy.mean(data[:,0] [:,1] [:,2] [:,3]) #defining meanfirstcol
print("Mean of First Column is:", meanfirstcol)



