import math

x = min(5, 10, 25)
y = max(5, 10, 25)
z = abs(-2.34)
a = pow(2, 4)
x = math.ceil(1.4)
y = math.floor(1.4)
PI = math.pi


try:
    if PI > 0:
        raise Exception("Sorry, no numbers below zero")
    if not type(PI) is str:
        raise TypeError("Only Str allow")
except Exception as err:
    print(err)
