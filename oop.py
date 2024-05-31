
class Student:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    
    def details(self):
        print(f"Name: {self.__name} & ID: {self.__id}.")


s1 = Student("Muna", 101)
s2 = Student("Jannatul", 102)

s1.details()
s2.details()