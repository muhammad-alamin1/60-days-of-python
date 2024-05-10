a = 12 + 2j # complex (Immutable )
b = ['a', 1, True, "false"] # list (mutable)
c = ('a', 1, True, "false") # tuple (Immutable )
d = {"name": "Muhammad", "age": 23, "address": "Betmore"} # dictonary (mutable)
e = {1, 2, 3} # set (mutable)
f = frozenset({1, 2, 3, 4, 5}) # (Immutable)
g = b"Hi" # (Immutable)
h = bytearray(b"Hi") # (mutable)

print(a)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(d["name"])
print(type(e))
print(type(f))
print(type(g))
print(type(h))