import sqlite3
import pandas as pd
from nba_py import league
import requests
from pandas import DataFrame

pd.set_option('display.max_columns', 500)

HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'
          }

base_url = 'http://stats.nba.com/stats/leaguedashplayerstats'

params = {"MeasureType":"Advanced","PerMode":"Totals","PlusMinus":"N","PaceAdjust":"N","Rank":"N","LeagueID":"00","Season":"2015-16","SeasonType":"Playoffs","PORound":0,"Outcome":'',"Location":'',"Month":0,"SeasonSegment":'',"DateFrom":'',"DateTo":'',"OpponentTeamID":0,"VsConference":'',"VsDivision":'',"TeamID":0,"Conference":'',"Division":'',"GameSegment":'',"Period":0,"ShotClockRange":'',"LastNGames":0,"GameScope":'',"PlayerExperience":'',"PlayerPosition":'',"StarterBench":'',"DraftYear":'',"DraftPick":'',"College":'',"Country":'',"Height":'',"Weight":''}

conn = sqlite3.connect('project/nba.db')
df = pd.read_sql_query("select * from gamelogs", conn)
df.sort_values(by = ['GAME_DATE'], ascending=[1])

for index, row in df.iterrows():
    date = row['GAME_DATE']
    print (date)
    params = {"MeasureType":"Advanced","PerMode":"Totals","PlusMinus":"N","PaceAdjust":"N","Rank":"N","LeagueID":"00","Season":"2015-16","SeasonType":"Regular Season","PORound":0,"Outcome":'',"Location":'',"Month":0,"SeasonSegment":'',"DateFrom":date,"DateTo":date,"OpponentTeamID":0,"VsConference":'',"VsDivision":'',"TeamID":0,"Conference":'',"Division":'',"GameSegment":'',"Period":0,"ShotClockRange":'',"LastNGames":0,"GameScope":'',"PlayerExperience":'',"PlayerPosition":'',"StarterBench":'',"DraftYear":'',"DraftPick":'',"College":'',"Country":'',"Height":'',"Weight":''}
    response = requests.get( base_url, params = params, headers = HEADERS )
    response.raise_for_status() # raise exception if invalid response
    values = response.json()['resultSets'][0]['rowSet']
    headers = response.json()['resultSets'][0]['headers']
    temp = DataFrame(values, columns=headers)
    print( temp.head() )
    break
