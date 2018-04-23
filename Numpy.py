# Claire Drummond 2018-04-23
# Iris Data Set Analysis
# Ref: Programming and Scripting Week 10 Videos

# Calculate the key statistics of each Column
import numpy

# Read data file into array
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
# picking the first column of data
firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
forthcol = data[:,3]

meanfirstcol = numpy.mean(data[:,0]) #defining meanfirstcol
print("Mean of First Column is:", meanfirstcol)
meansecondcol = numpy.mean(data[:,1]) #defining meansecondcol
print("Mean of Second Column is:", meansecondcol)
meanthirdcol = numpy.mean(data[:,2]) #defining meanthirdcol
print("Mean of Third Column is:", meanthirdcol)
meanforthcol = numpy.mean(data[:,3]) #defining meanforthcol
print("Mean of Forth Column is:", meanforthcol)

medianfirstcol = numpy.median(data[:,0]) #defining medianfirstcol
print("Median of First Column is:", medianfirstcol)
mediansecondcol = numpy.median(data[:,1]) #defining mediansecondcol
print("Median of Second Column is:", mediansecondcol)
medianthirdcol = numpy.median(data[:,2]) #defining medianthirdcol
print("Median of Third Column is:", medianthirdcol)
medianforthcol = numpy.median(data[:,3]) #defining medianforthcol
print("Median of Forth Column is:", medianforthcol)

stdfirstcol = numpy.std(data[:,0]) #defining stdfirstcol
print("Standard Deviation of First Column is:", stdfirstcol)
stdsecondcol = numpy.std(data[:,1]) #defining stdsecondcol
print("Standard Deviation of Second Column is:", stdsecondcol)
stdthirdcol = numpy.std(data[:,2]) #defining stdthirdcol
print("Standard Deviation of Third Column is:", stdthirdcol)
stdforthcol = numpy.std(data[:,3]) #defining stdforthcol
print("Standard Deviation of Forth Column is:", stdforthcol)

maxfirstcol = numpy.max(data[:,0]) #defining maxfirstcol
print("Maximum of First Column is:", maxfirstcol)
maxsecondcol = numpy.max(data[:,1]) #defining maxsecondcol
print("Maximum of Second Column is:", maxsecondcol)
maxthirdcol = numpy.max(data[:,2]) #defining maxthirdcol
print("Maximum of Third Column is:", maxthirdcol)
maxforthcol = numpy.max(data[:,3]) #defining maxforthcol
print("Maximum of Forth Column is:", maxforthcol)

minfirstcol = numpy.min(data[:,0]) #defining minfirstcol
print("Minimum of First Column is:", minfirstcol)
minsecondcol = numpy.min(data[:,1]) #defining minsecondcol
print("Minimum of Second Column is:", minsecondcol)
minthirdcol = numpy.min(data[:,2]) #defining minthirdcol
print("Minimum of Third Column is:", minthirdcol)
minforthcol = numpy.min(data[:,3]) #defining minforthcol
print("Minimum of Forth Column is:", minforthcol)