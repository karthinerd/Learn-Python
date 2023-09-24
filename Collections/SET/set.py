# Set is a collection which is unordered, unchangeable*, and unIndexed. No duplicate members.

sets = {'karthi',10,False,"karthi",0,True,1}

print(sets)

# Find Length

print(len(sets))

# Another Way to Create SET

anotherSet = set(("abc", "def", "ghi"))


# Once a set is created, you cannot change its items, but you can add new items. #

# Add one Item

anotherSet.add("jkl")

print(anotherSet)

# UPDATE Add Any Iterable Object

lists = [1,3,4,2,5]

sets.update(lists)

print(sets)

# Remove - If the item to remove does not exist, remove() will raise an error.

sets.remove("karthi")

print(sets)

# Discard - If the item to remove does not exist, discard() will NOT raise an error.

sets.discard("a")

print(sets)

# Clear 

sets.clear()

print(sets)

# Delete

del sets

print(sets)