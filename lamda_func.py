def _addition(n):
    return lambda a : a + n

result = _addition(5)
print(result(7))