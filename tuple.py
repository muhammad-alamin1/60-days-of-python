t = tuple((2, "muna", 5, "Jannatul"))
add_t = ("Israt",)

t_list = list(t)
t_list[0] = "Mimi"
t = tuple(t_list)
t += add_t
t = list(t)
t.remove(5)

(w, x, *y, z) = t

for i in range(len(t)):
    print(t[i])

print(t.index("Jannatul"))

