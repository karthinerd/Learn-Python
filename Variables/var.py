# Variables Declaration
a = 3
b = "karthi"
c = 2.10

_name_ = "Raj"

lastName = "kumar"

# Output a Variable
print(_name_)

# Unpack a Collection
brother,mySelf,Mummy = "rajkumar","karthi","latha"

print("My mother name is - ",Mummy)

# One Value to Multiple Variables 
myKing = MyDad = "rajendran"

print("My father name is - ",myKing)

# Global Variable 

x = 10 #By Default Global Scope

def sum():
    x = 20  #By Default Local Scope inside function 
    # but we can make it as global by Using "Global" Keyword
    # global x 
    print('Local ---> ',x)
    
sum()

print('Global --> ',x)