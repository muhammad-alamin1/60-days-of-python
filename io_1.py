# print("Hello", "World", sep=" & ", end="\n")
# string concat
first_name = "Muhammad"
last_name = "Al- AMin"

full_name = first_name + " " + last_name
# print(full_name)

# print file 
for i in range(5):
    with open("python.txt", "w") as file:
        print("Free Palestine", end=".", file=file, flush=False)