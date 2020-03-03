import pymongo
import pprint

pp = pprint.PrettyPrinter(indent=2)

database = pymongo.MongoClient("mongodb://localhost:27017")

bballDB = database["collegeBasketball"]

conf = input("Please enter a conference (camelcase, no spaces: ex: big12, bigEast): ")
visitor = input("Please enter the away team: ")
home = input("Please enter the home team: ")

def games(conf, visitor, home):
  conference = bballDB[conf].find()

  homePoints = 0
  homeGames = []
  homeOppTotalPoints = 0
  awayPoints = 0
  awayGames = []
  awayOppTotalPoints = 0

  for item in conference:
    if item["Home"] == home and item["HOMEPTS"] != '':
      homeGames.append(item)
      if item["HOMEPTS"] != '':
        homePoints += item["HOMEPTS"]
    if item["Visitor"] == visitor and item["AWAYPTS"] != '':
      awayGames.append(item)
      if item["AWAYPTS"] != '':
        awayPoints += item["AWAYPTS"]

  for item in homeGames:
    homeOppTotalPoints += item["AWAYPTS"]
  
  for item in awayGames:
    awayOppTotalPoints += item["HOMEPTS"]


  info = {
    'homeTeam': home,
    'ppgHome': homePoints / len(homeGames),
    'homeOppPPG': homeOppTotalPoints / len(homeGames),
    'homeTotals': (homePoints / len(homeGames) + homeOppTotalPoints / len(homeGames)),
    'homeMargin': (homePoints / len(homeGames) - homeOppTotalPoints / len(homeGames)),
    'awayTeam': visitor,
    'ppgAway': awayPoints / len(awayGames),
    'awayOppPPG': awayOppTotalPoints / len(awayGames),
    'awayTotals': (awayPoints / len(awayGames) + awayOppTotalPoints / len(awayGames)),
    'awayMargin': (awayPoints / len(awayGames) - awayOppTotalPoints / len(awayGames))
  }

  return info

print(games(conf, visitor, home))