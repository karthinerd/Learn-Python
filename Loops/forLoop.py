#  PRIMITIVE LOOP

name = "rajkumar"

for x in name :
    print(x)
    
name = "karthi"

rn = name[::-1]

# Reverse Loop
for i in range(len(rn)) :
    print(rn[i])

# Short - Hand Reverse String
print(name[::-1])


# Range 

for x in range(0,20,2) :
    if x == 0 : continue
    print(x)
else :  # else not works when using "break" statement
    print("Finally!!!")

# Nested For Loop

tup = ("a","b","c")

ls = ["d","e","f"]

for x in tup :
    for y in ls :
     print(x,y)
