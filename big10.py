import pymongo

database = pymongo.MongoClient("mongodb://localhost:27017")

bballDB = database["collegeBasketball"]

big10 = bballDB["big10"].find()

homePoints = 0
homeGames = []
awayPoints = 0
awayGames = []

for item in big10:
  if item["Home"] == "Rutgers":
    homeGames.append(item)
    if item["HOMEPTS"] != '':
      homePoints += item["HOMEPTS"]

print(homePoints)
print(homeGames)