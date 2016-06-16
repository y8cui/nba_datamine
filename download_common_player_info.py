import requests
import sqlite3

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

#http://stats.nba.com/stats/commonplayerinfo?LeagueID=00&PlayerID=1626143&SeasonType=Regular+Season

conn = sqlite3.connect('project/nba.db')
c = conn.cursor()

c.execute("CREATE TABLE players_common_info (PERSON_ID integer,\
                                             BIRTHDAY text,\
                                             WEIGHT text,\
                                             HEIGHT text,\
                                             POSITION text)")


player_common_info_base_url = "http://stats.nba.com/stats/commonplayerinfo"
for player in players:
    player_id = player[0]
    season_type = "Regular Season"
    params = {'PlayerID': player_id, 'LeagueID': league_id, 'SeasonType': season_type}
    response = requests.get( player_common_info_base_url, params = params, headers = HEADERS )
    response.raise_for_status() # raise exception if invalid response
    player_common_info = response.json()['resultSets'][0]['rowSet'][0]
    c.execute('INSERT INTO players_common_info VALUES (?,?,?,?,?)', 
	(player_common_info[0],
    player_common_info[6],
    player_common_info[10],
    player_common_info[11],
    player_common_info[14]))

conn.commit()
conn.close()


