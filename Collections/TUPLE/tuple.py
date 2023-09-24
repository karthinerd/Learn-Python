# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

tuples = ("a","b","c","a",True,10)

# create a tuple with only one item, you have to add a comma after the item

tup = ("a",)

# Access

print(tuples[1])

# Type

print(type(tup))

#  Length

print(len(tuples))

# ADD Tuple to Tuple

tupleTwo = (1,2,3,4)

tuples += tupleTwo

print(tuples)

# Update Tuple - Convert into list - Perform All Methods in List - convert Back To Tuple

tupleConvert  = list(tuples)

tupleConvert[0] = "alpha"

tuples = tuple(tupleConvert)

print(tuples)

# UnPack Tuples

x = y = z = tuples

print(x,y,z)

a,b,*c = tuples

print(a,b,c)

tupleThree = tupleTwo * 2 

print(tupleThree)