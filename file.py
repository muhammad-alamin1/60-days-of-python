import os.path

if os.path.isfile("./dem.txt"):
    with open("./demo.txt", "r") as file:
        line = file.readline()
        while line != '':
            print(line, end = '')
            line = file.readline()
else:
    print("File Doesn't exists.!")