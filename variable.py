fruits = ["apple", "Mango", "Banana"]
x, y, z = fruits

a = "python"

def _my_func():
    global a
    a = "C++"
    print(a)

print(x, y, z)
_my_func()
print(a)