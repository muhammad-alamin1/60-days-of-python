str = " The best things in life are free! "
name_age = "Muhammad Al-Amin 23"

print(str)
print("best" not in str)
print(str[3:8])
print(str.strip()) # remove space starting & ending point

split_name = name_age.split(" ")
identity = f"My name is {split_name[0]} & age {split_name[2]}."
encode = str.encode()
print(encode)

