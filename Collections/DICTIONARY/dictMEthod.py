
keyValue = {
    "home" : "Rent",
    "laptop" : "HP" ,
    "Car" : False,
    "Bike" : True
}

# POP

keyValue.pop("Car")

print(keyValue)

# PopItem - Removes Last Item

keyValue.popitem()

print(keyValue)
    
# Delete

del keyValue["home"]

print(keyValue)

# del keyValue

print(keyValue)

# Clear

keyValue.clear()

print(keyValue)

# COPY

dictCopy = keyValue.copy()

print(dictCopy)

#   or   #

subDict = dict(keyValue)

print(subDict)

# Nested Dictionary

myFamily = {
  "child3" : {
    "name" : "karthi",
    "year" : 2002
  },
  "child2" : {
    "name" : "kumar",
    "year" : 1998
  },
  "mother" : {
    "name" : "latha",
    "year" : 1973
  }
}

# Access Nested Dictionary

print(myFamily["child3"]["name"])


