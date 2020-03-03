import pymongo
import pprint

pp = pprint.PrettyPrinter(indent=2)

database = pymongo.MongoClient("mongodb://localhost:27017")

bballDB = database["collegeBasketball"]



def games(conf, visitor, home):
  conference = bballDB[conf].find()

  homePoints = 0
  homeGames = []
  awayPoints = 0
  awayGames = []

  for item in conference:
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

print(games("acc", "Syracuse", "Boston College"))