# Dictionary is a collection which is ordered** and changeable. No duplicate members. #

# Dictionaries are used to store data values in key:value pairs. #

# Duplicate values will overwrite existing values #
dictionary = {
    "name" : "Karthi",
    "age" : 20 ,
    "adult" : True ,
    "age" : 21 ,
    "about" : ["junior","Python","Developer"]
}

print(dictionary)

# Another Way to Create Dictionary

d = dict(name="Kumar" , age = 24)

print(type(d))

# Find Length

print(len(dictionary))

# Access

print(dictionary["name"])

print(dictionary.get("age"))

# Keys

print(dictionary.keys())

# values

print(dictionary.values())

# Item - key : value

print(dictionary.items())

# Check IN

if "age" not in dictionary:
    print("Age is present")
    
# Change Item 

d["age"] = 25

print(d)

# Update

dictionary.update({"hobbies":"Cricket"})

print(dictionary)

# Add

dictionary["gender"] = "Male"

print(dictionary)