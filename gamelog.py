import requests
import sqlite3

conn = sqlite3.connect('nba.db')
c = conn.cursor()

#http://stats.nba.com/stats/leaguegamelog?Counter=1000&Direction=DESC&LeagueID=00&PlayerOrTeam=P&Season=2015-16&SeasonType=Regular+Season&Sorter=PTS

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

response = requests.get( gamelog_base_url, params = params )
response.raise_for_status() # raise exception if invalid response


