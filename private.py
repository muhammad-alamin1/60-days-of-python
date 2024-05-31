class MyClass:
    def __init__(self, product, value):
        self.__private_property = value  # Private property
        self._product = product         # protected property
    
    @property
    def name(self):
        return self.__product
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Value must be string.")
        self.__product = name


obj = MyClass(None, None)

try:
    #print(obj.__private_property) error
    obj.name = "CCTV"
    print(obj.name)
except AttributeError as e:
    print(e)  # Output: 'MyClass' object has no attribute '__private_property'