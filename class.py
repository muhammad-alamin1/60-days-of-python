
# Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name} & Age: {self.age}"
    
    def display(self):
        print(f"Hello there! My name is {self.name} & age {self.age}")

# student class
class Student:
    def __init__(self):
        print(self)
    
    def my_fun(self, name):
        print(name)


p = Person("Muhammad", 23)
s1 = Student()

print(s1.my_fun("Muhammad"))
