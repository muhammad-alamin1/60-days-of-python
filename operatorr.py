# exponentiation

x = 16
y = 5

z = x ** y
a = x / y
b = x // y
# print(z, a, b)

# logical operation
x = True
y = False

'''
print(x and y)
print(x or y)
print(not y)
'''

age = 18
has_ticket = True

can_enter_movie = age >= 18 and has_ticket
print(can_enter_movie)

cannot_enter_movie = age < 18 or not has_ticket
print(cannot_enter_movie)

bal = 200
bal += (bal*5)/100
print(bal)