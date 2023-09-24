# The word "polymorphism" means "Many Forms" #

#  it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


# LEN() is a common MEthod to find LENGTH

ls = ["a",2,True]

print(len(ls))

# In Class & Inheritance

class parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class child1(parent):
    def get_age(self):
        return f"{self.name}, Age {self.age}"
    
class child2(parent):
    def get_age(self):
        return f"{self.name}, Age {self.age}"
    
obj1 = child1("karthi", 21)
obj2 = child2("kumar", 25)

for x in (obj1, obj2):
    print(x.get_age())
