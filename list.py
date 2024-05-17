arr = [1, 3, True, (47, "Muna")]
girl_friend_list = list(("Sneha", "Farah", "Israt", "Muna", "Muna", "Jannatul"))
this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
l = arr[-1][-1]

girl_friend_list.insert(len(girl_friend_list), "Ferdousi")
girl_friend_list.append("Nur")
girl_friend_list.insert(0, "Mimi")
this_list.extend(tropical)

print(girl_friend_list)

girl_friend_list.remove("Muna")
this_list.clear()

i = 0
while i < len(tropical):
    print(tropical[i])
    i += 1

print(girl_friend_list)
print(this_list)

# list comprehension
[print(x) for x in girl_friend_list]
girl_friend_list.sort(reverse = True)
print(girl_friend_list)