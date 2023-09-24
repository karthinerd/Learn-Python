# PYTHON - Object Oriented Programming language #

# Class is like an object constructor, or a "blueprint" for creating objects #

# CLASS

class my_class :
    x = 5
    print("HI")
    
my_class()

# Object Creation

obj = my_class()

print(obj.x)

# __init__() Function  ---> which is always executed when the class is being initiated

class init_class :
    def __init__(self,name,age) :
# SELF ---> parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
        
        self.name = name
        self.age = age
        
#  __str__() ---> function controls what should be returned when the class object is represented as a string.
    
    def __str__(self) :
        return f"{self.name} - ({self.age})"
    
# Objects can also contain METHODS. Methods in objects are functions that belong to the object

    def fun_method(self) :
        return f"Hi {self.name}"
    
        
init_obj = init_class("raj",25)

print(init_obj.age)

print(init_obj)

print(init_obj.fun_method())

# Modify Object Properties

init_obj.age = 26

print(init_obj.age)

# Delete Object Properties

del init_obj.age

print(init_obj)

# Delete Object

del init_obj

print(init_obj)