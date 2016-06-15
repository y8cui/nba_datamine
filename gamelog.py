import requests

#http://stats.nba.com/stats/leaguegamelog?Counter=1000&Direction=DESC&LeagueID=00&PlayerOrTeam=P&Season=2015-16&SeasonType=Regular+Season&Sorter=PTS
HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'
          }

gamelog_base_url = 'http://stats.nba.com/stats/leaguegamelog'
league_id = '00' #nba league id
season = '2015-16' #nba season
seasonType = 'Regular Season'
PlayerID = 2546

params = {'Counter': 1000, 
          'Direction': 'DESC', 
          'LeagueID': league_id, 
          'PlayerOrTeam': 'P',
          'Season': '2015-16',
          'SeasonType': 'Regular Season',
          'Sorter': 'PTS'
         }

response = requests.get( gamelog_base_url, params = params, headers = HEADERS )
response.raise_for_status() # raise exception if invalid response
gamelogs = response.json()['resultSets'][0]['rowSet']

f = open("gamelogs.txt", "w")
for log in gamelogs:
  f.write("%s\n" % log)
f.close()


