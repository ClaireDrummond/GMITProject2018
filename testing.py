with open("data/iris.csv") as f:
    size_to_read = 10 # this shows 10 characters at a time

    f_contents = f.read(size_to_read) 
    print(f_contents, end='') # this shows the first 10 characters

    f.seek(0)

    f_contents = f.read(size_to_read) 
    print(f_contents, end='') # this shows the second 10 characters 

 