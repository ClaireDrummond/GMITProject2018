import csv #importing the csv module

with open("data/iris.csv", "r") as f:
  reader = csv.reader(f) # creating a variable reader
  for line in reader:
    print(line)

with open("data/iris.csv", "r") as f:
  reader = csv.reader(f) # creating a variable reader
  for line in reader:
    print(line[4]) # this prints the 5th Varaiable of each row