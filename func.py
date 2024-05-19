def my_function(*kids):
    print("The youngest child is " + kids[2])
    print("The youngest child is ", *kids)

def my_function1(**kid):
    print("His fast name is " + kid["fname"])

my_function("Emil", "Tobias", "Linus")
my_function1(fname = "Tobias", lname = "Refsnes")

