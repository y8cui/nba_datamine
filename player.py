import requests

#http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=1&LeagueID=00&Season=2015-16

player_base_url = 'http://stats.nba.com/stats/commonallplayers'
league_id = '00' #nba league id
season = '2015-16' #nba season

params = {'IsOnlyCurrentSeason': 1, 'LeagueID': league_id, 'Season': season}
response = requests.get( player_base_url, params = params )
response.raise_for_status() # raise exception if invalid response
players = response.json()['resultSets'][0]['rowSet']

f = open("test.txt", "w")
for player in players:
  f.write("%s\n" % player)
f.close()
