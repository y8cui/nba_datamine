import requests

HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'
          }
#http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=1&LeagueID=00&Season=2015-16

player_base_url = 'http://stats.nba.com/stats/commonallplayers'
league_id = '00' #nba league id
season = '2015-16' #nba season

params = {'IsOnlyCurrentSeason': 1, 'LeagueID': league_id, 'Season': season}
response = requests.get( player_base_url, params = params, headers = HEADERS )
response.raise_for_status() # raise exception if invalid response
players = response.json()['resultSets'][0]['rowSet']

f = open("players.txt", "w")
for player in players:
  f.write("%s\n" % player)
f.close()
