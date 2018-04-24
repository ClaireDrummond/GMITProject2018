# Claire Drummond 2018-04-01
# Applying Code from Ref: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files to Iris Data Set

with open("data/iris.csv") as f: # opens and closes (once script has run) file iris
    print (f.read()) # dispays all contents of file


with open("data/iris.csv") as f:
    print (f.readline()) # reads the first line of the file
    print (f.readline()) # reads the second line of the file
    print (f.readline()) # reads the third line of the file and so on.....


with open("data/iris.csv") as f:
    for line in f:
        print(line, end='') # instead of reading the file line by line, this is another method of viewing the whole file

with open("data/iris.csv") as f:
    size_to_read = 10 # this shows 10 characters at a time

    f_contents = f.read(size_to_read) 
    print(f_contents, end='') # this shows the first 10 characters

    f_contents = f.read(size_to_read) 
    print(f_contents, end='') # this shows the second 10 characters   

    f_contents = f.read(size_to_read) 
    print(f_contents, end='') # this shows the third 10 characters
    
    f.seek(0) # instead of picking up where the script left off, setting seek to 0, tells the script to go back to the start of the file

   







