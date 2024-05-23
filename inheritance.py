class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def full_name(self):
        return f"{self.fname} {self.lname}"


# student class
class Student(Person):
    def __init__(self, fname, lname, g_year):
        super().__init__(fname, lname)
        self.graduationyear = g_year

    def welcome(self):
        return f"Welcome {self.fname} {self.lname} to the class of {self.g_year}"

p1 = Person("Muhammad", "Al-Amin")

full_name = p1.full_name()
print(full_name)