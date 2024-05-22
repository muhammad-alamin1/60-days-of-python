import os.path

if os.path.isfile("demo.txt"):
    with open("demo.txt", "a+", encoding="utf-8") as fp:
        print(fp.tell())
        fp.write("I Am new line")
        print(fp.tell())


