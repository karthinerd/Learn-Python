# If Loop

a = 50

b = 6

if a>b :
    print("a is greater than b")
    
# Short - Hand #

if b<a : print("B less than A")
    
# If - Else

name = "karthigairaj"

if "karthi" in name :
    print("Hi Karthi")
else:
 print("Hi Friend")
 
# Short - Hand #
 
print("hi karthigairaj") if "Kar" in name else print("Hi , What's your name ?")
 
# El-If

tup = ("apple","banana","Mango","cherry")

if "cherry" not in tup :
    print("Miss Cherry")
elif a>len(tup) :
    print(f"a({a}) is bigger than tup({len(tup)})")
else :
    print("Different Fruits")
    
x , y , z = 3 , 6 , 9
    
# AND


if x<y and y<z :
    print("Condition Satisfied")
    
# OR

if x==y or z/x==3 :
    print("One is True")
    
# NOT

if not x>z :
    print("Result Reversed")
    
# Nested - If

if x<z :
    print("Big X")
    if x<y :
        print("Small x")
    else :
        print("Waste x")