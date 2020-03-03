import pymongo

database = pymongo.MongoClient("mongodb://localhost:27017")

bballDB = database["collegeBasketball"]

x = bballDB["acc"].find()

for item in bballDB["acc"].find():
  if item["Home"] == "Duke":
    print(item)