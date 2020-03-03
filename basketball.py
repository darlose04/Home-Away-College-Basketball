import pymongo

database = pymongo.MongoClient("mongodb://localhost:27017")

bballDB = database["collegeBasketball"]

x = bballDB["acc"].find()

awayPoints = 0

for item in bballDB["acc"].find():
  awayPoints += item["AWAYPTS"]

print(awayPoints)