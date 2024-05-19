import os

file = open("./demo.txt", "a")

file.write("Now the file has more content!")
file.close()

file = open("./demo.txt", "r")

buffer = file.read()
print(buffer)
file.close()

try:
    if os.path.exists("./demo.txt"):
        os.remove("./demo.txt")
    else:
        print("File doesn't exists.\n")
except Exception as err:
    print("Exception Caught: ", err)
else:
    print("File Delete successfully.\n")