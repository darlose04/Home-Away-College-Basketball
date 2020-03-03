import pymongo
import pprint

pp = pprint.PrettyPrinter(indent=2)

database = pymongo.MongoClient("mongodb://localhost:27017")

bballDB = database["collegeBasketball"]

big10 = bballDB["big10"].find()

def games(visitor, home):
  homePoints = 0
  homeGames = []
  awayPoints = 0
  awayGames = []

  for item in big10:
    if item["Home"] == home:
      homeGames.append(item)
      if item["HOMEPTS"] != '':
        homePoints += item["HOMEPTS"]

  for item in big10:
    if item["Visitor"] == visitor:
      awayGames.append(item)
      if item["AWAYPTS"] != '':
        awayPoints += item["AWAYPTS"]

  print(homePoints / 9)
  pp.pprint(homeGames)

  print(awayPoints)
  pp.pprint(awayGames)

# print(games("Maryland", "Rutgers"))