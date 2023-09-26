#  NoSQL database is MongoDB

# MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable


# Python needs a MongoDB driver ("PyMongo") to access the MongoDB database.

import pymongo


# create database

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

database = myClient["python-mongo"]


# Check if Database Exists


checkDb = myClient.list_database_names()

print(checkDb)

if "EmployeeDB" in checkDb :
    print("Yes")
    
# A collection in MongoDB is the same as a table in SQL databases.

collection = database["learn-pymongo"]

# Check Collection

checkCollection = database.list_collection_names()

print(checkCollection)

# A document in MongoDB is the same as a record in SQL databases.'

# insert_one()

myDicts = {"_id":1,"name":"Karthi","age":20}

ins = collection.insert_one(myDicts)

print(ins.inserted_id)

# insert_many()

myList = [
  { "_id": 2, "name": "Peter", "address": "street 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

insMany = collection.insert_many(myList)

print(insMany.inserted_ids)

# FIND

# In MongoDB we use the find() and find_one() methods to find data in a collection

f1 = collection.find_one() 

print(f1)

print(checkCollection)

# Find All

f2 = collection.find()

print(f2)

for x in collection.find() :
    print(x)

# Return Only Some Fields
# The second parameter of the find() method is an object describing which fields to include in the result
print("Some")

for x in collection.find({},{"_id":0,"name":1,"address":1}) :
    print(x)
    
# The first argument of the find() method is a query object, and is used to limit the search

my_query = {"name":"Amy"}

for x in collection.find(my_query) :
    print(x)
    
# Advanced Query

# find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}
print("Advance")

adv_query = {"address" : {"$gt":"S"}}

for x in collection.find(adv_query) :
    print(x)
    
# RegEx Query

# Find documents where the address starts with the letter "S"

print("Regular Expression")

regEx_query = {"address":{"$regex":"^S"}}

for x in collection.find(regEx_query) :
    print(x)
    
# SORT

# sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction)

print("Sort")

#  1 ---> Ascending
# -1 ---> Descending

my_sort = collection.find().sort("name",-1)

for x in my_sort:
    print(x)
    
# Update

print("update")

# If the query finds more than one record, only the first occurrence is updated.

# first parameter of the update_one() method is a query object defining which document to update
# second parameter is an object defining the new values of the document

fq = {"address":"street 27"}

# $set operator is used to update specific fields within a document 

uv = {"$set":{"address":"street 36"}}
    
collection.update_one(fq,uv)

for x in collection.find() :
    print(x)
    
# Update MANY

eq = {"address":{"$regex":"^S"}}

nv = {"$set":{"address":"Karthi"}}

res = collection.update_many(eq,nv)

print(res.modified_count," was modified")

# LIMIT

# limit() method takes one parameter, a number defining how many documents to return

print("Limit")

limit_res = collection.find().limit(5)

for x in limit_res:
    print(x)

# Delete

# The first parameter of the delete_one() method is a query object defining which document to delete

delete_query = {"name":"Karthi"}

d = collection.delete_one(delete_query)

print(d)

print("Delete")

for x in collection.find() :
    print(x)
    

# Delete MANY

many_dlt = {"address":{"$regex":"^S"}}

dm = collection.delete_many(many_dlt)

print(dm.deleted_count," deleted")


# Delete All Documents

all_dlt = collection.delete_many({})

print(all_dlt.deleted_count," was deleted")

# Drop Collection

# drop() method returns true if the collection was dropped successfully, and false if the collection does not exist

collection.drop()

