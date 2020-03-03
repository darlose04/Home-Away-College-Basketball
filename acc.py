import pymongo

database = pymongo.MongoClient("mongodb://localhost:27017")

bballDB = database["collegeBasketball"]

x = bballDB["acc"].find()

acc = bballDB["acc"].find()

awayPoints = 0
homePoints = 0

accArr = []

for item in acc:
  if item["AWAYPTS"] != '':
    awayPoints += item["AWAYPTS"]
  if item["HOMEPTS"] != '':
    homePoints += item["HOMEPTS"]
  accArr.append(item)



# entry = bballDB["acc"].find_one()
# print(entry["AWAYPTS"])
# print(type(entry["AWAYPTS"]))


print("Visitor total points: ", awayPoints)
print("Home total points: ", homePoints)
print(len(accArr))