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
    if item["Home"] == home and item["HOMEPTS"] != '':
      homeGames.append(item)
      if item["HOMEPTS"] != '':
        homePoints += item["HOMEPTS"]
    if item["Visitor"] == visitor and item["AWAYPTS"] != '':
      awayGames.append(item)
      if item["AWAYPTS"] != '':
        awayPoints += item["AWAYPTS"]

  info = {
    'homeTeam': home,
    'ppgHome': homePoints / len(homeGames),
    'awayTeam': visitor,
    'ppgAway': awayPoints / len(awayGames)
  }

  return info

print(games("Maryland", "Rutgers"))
# print(games("Michigan State", "Penn State"))