import requests
import sqlite3

HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'
          }

#http://stats.nba.com/stats/leaguegamelog?Counter=1000&Direction=DESC&LeagueID=00&PlayerOrTeam=T&Season=2015-16&SeasonType=Regular+Season&Sorter=PTS

team_gamelog_base_url = 'http://stats.nba.com/stats/leaguegamelog'
league_id = '00' #nba league id
season = '2015-16' #nba season
season_type = "Regular Season"
sorter = "PTS"
PlayerOrTeam = "T"
Direction = "DESC"

params = {'PlayerOrTeam': PlayerOrTeam, 'LeagueID': league_id, 'Season': season,
          'Sorter': sorter, 'Direction': Direction, 'SeasonType': season_type}
response = requests.get( team_gamelog_base_url, params = params, headers = HEADERS )
response.raise_for_status() # raise exception if invalid response
team_gamelogs = response.json()['resultSets'][0]['rowSet']



conn = sqlite3.connect('project/nba.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS team_gamelogs");
c.execute("CREATE TABLE team_gamelogs       (SEASON_ID text,\
                                             TEAM_ID integer,\
                                             TEAM_ABBREVIATION text,\
                                             TEAM_NAME text,\
                                             GAME_ID text,\
                                             GAME_DATE text,\
                                             MATCHUP text, \
                                             WL text,\
                                             MIN integer,\
                                             FGM integer, \
                                             FGA integer, \
                                             FG_PCT integer, \
                                             FG3M integer ,\
                                             FG3A integer ,\
                                             FG3_PCT integer ,\
                                             FTM integer ,\
                                             FTA integer ,\
                                             FT_PCT integer ,\
                                             OREB integer ,\
                                             DREB integer ,\
                                             REB integer ,\
                                             AST integer ,\
                                             STL integer ,\
                                             BLK integer ,\
                                             TOV integer ,\
                                             PF integer ,\
                                             PTS integer ,\
                                             PLUS_MINUS integer, \
                                             VIDEO_AVAILABLE integer)")

for log in team_gamelogs:
    print (len(log))
    print (log)
    c.execute('INSERT INTO team_gamelogs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', 
	log)

conn.commit()
conn.close()

