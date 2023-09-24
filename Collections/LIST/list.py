# List items are ordered, changeable, and allow duplicate values #

listOne = ["a",1,True,"a"]

print(type(listOne))

# Access

print(listOne[2])

print(listOne[-4:-1])  # ---> Last Index Not Included - ( n - 1 )

# Find Length

print(len(listOne))

# Another Way To Create LIST
newList = list(("a","b","c"))

print(newList)

# list(()) is a useful construct in Python for converting iterable objects into lists #

my_tuple = ("apple", "banana", "cherry") #---> TUPLE
my_list = list(my_tuple)  #--> Convert into list

print(my_list)

# Check - IN

if "apple" in my_list:
    print("Yes")

#  NOT - IN

if "karthi" not in my_list :
    print("Karthi not there...")
    
# Change List

my_list[0] = "Grape"

print(my_list)

my_list[:2] = ["pomegranate","Mango"]

print(my_list)

