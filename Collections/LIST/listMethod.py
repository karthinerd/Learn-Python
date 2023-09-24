
my_collection = ["Home","Cycle","Bike"]

# Insert a New Item at Specified INDEX

my_collection.insert(1,"Car")

print(my_collection)

# Append add New Item at Last INDEX

my_collection.append("Water")

print(my_collection)

# Remove specified Item

my_collection.remove("Water")

print(my_collection)

# Extend - Add Any Iterable

my_new_collection = ["playstation","GTA"]

my_collection.extend(my_new_collection)

print(my_collection)

# JOIN 

collection = my_collection + my_new_collection

print("Join",collection)

# POP - If you do not specify the index, the pop() method removes the last item.

my_collection.pop(1)

print(my_collection)

# DELETE 

del my_collection[3]

print(my_collection)

# del my_collection

# print(my_collection)  # ---> Raise an Error

# CLEAR 

my_collection.clear()

print(my_collection)

numbers = [11,287,340,44,57,10,877]

alpha = ['c','b','a',"A","C","B"]

# SORT

numbers.sort()

print(numbers)

alpha.sort()

print(alpha)

alpha.sort(key=str.lower)

print(alpha)

# SORT REVERSE

numbers.sort(reverse=True)

print(numbers)

# Reverse Order

my_new_collection.reverse()

print("Reverse",my_new_collection)

# COPY

makeCopy = numbers.copy()

print(makeCopy)

    # or #

clone = list(alpha)

print(clone)