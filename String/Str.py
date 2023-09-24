my_name = "karthi"

# Multi - line Use ---> "" or ''

intro = """"
hi , i am karthi from madurai,
i am software Developer
"""

print(intro)

# Strings in Python are arrays of bytes representing unicode characters #

# Access String

print(my_name[0])

# Find Length

print(len(my_name))

# Loop a String

for x in my_name:
    print(x)
    
# Check String ---> PRESENT

print("kar" in my_name)

#    or    #

if "thi" in my_name :
    print("YES")
    

# NOT PRESENT

print ("raj" not in my_name)


#    or    #

if "gai" not in my_name :
    print("NO")
    
    
myFullName = "Karthigairaj"

# SLICE

print("People Call Me --->",myFullName[:6])

print(myFullName[1:])

print(myFullName[-5:-1])