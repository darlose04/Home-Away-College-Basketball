import pymongo

database = pymongo.MongoClient("mongodb://localhost:27017")

bballDB = database["collegeBasketball"]

big10 = bballDB["big10"].find()