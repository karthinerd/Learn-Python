from python_MongoDb import database as db

collection = db["py-md"]

cc = db.list_collection_names()

print(cc)

