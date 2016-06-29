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
df = df.sort_values(by = ['GAME_DATE', 'TEAM_ABBREVIATION','PLAYER_NAME'], ascending=[1,1,1])

old_date = ''
for index, row in df.iterrows():
    date = row['GAME_DATE']
    #if date > "2015-11-01":
    #    break
    if (date != old_date):
        print (date)
        old_date = date
        params = {"MeasureType":"Advanced","PerMode":"Totals","PlusMinus":"N","PaceAdjust":"N","Rank":"N","LeagueID":"00","Season":"2015-16","SeasonType":"Regular Season","PORound":0,"Outcome":'',"Location":'',"Month":0,"SeasonSegment":'',"DateFrom":date,"DateTo":date,"OpponentTeamID":0,"VsConference":'',"VsDivision":'',"TeamID":0,"Conference":'',"Division":'',"GameSegment":'',"Period":0,"ShotClockRange":'',"LastNGames":0,"GameScope":'',"PlayerExperience":'',"PlayerPosition":'',"StarterBench":'',"DraftYear":'',"DraftPick":'',"College":'',"Country":'',"Height":'',"Weight":''}
        response = requests.get( base_url, params = params, headers = HEADERS )
        response.raise_for_status() # raise exception if invalid response
        values = response.json()['resultSets'][0]['rowSet']
        headers = response.json()['resultSets'][0]['headers']
        temp = DataFrame(values, columns=headers)
    
    temp_row = temp.loc[temp['PLAYER_ID'] == row['PLAYER_ID']].iloc[0]
    if temp_row['PLAYER_ID'] != row['PLAYER_ID']:
        continue
    df.set_value(index, "TEAM_ABBREVIATION", temp_row["TEAM_ABBREVIATION"])
    df.set_value(index, "AGE", temp_row["AGE"])
    df.set_value(index, "OFF_RATING", temp_row["OFF_RATING"])
    df.set_value(index, "DEF_RATING", temp_row["DEF_RATING"])
    df.set_value(index, "NET_RATING", temp_row["NET_RATING"])
    df.set_value(index, "AST_PCT", temp_row["AST_PCT"])
    df.set_value(index, "AST_TO", temp_row["AST_TO"])
    df.set_value(index, "AST_RATIO", temp_row["AST_RATIO"])
    df.set_value(index, "OREB_PCT", temp_row["OREB_PCT"])
    df.set_value(index, "DREB_PCT", temp_row["DREB_PCT"])
    df.set_value(index, "REB_PCT", temp_row["REB_PCT"])
    df.set_value(index, "TM_TOV_PCT", temp_row["TM_TOV_PCT"])
    df.set_value(index, "EFG_PCT", temp_row["EFG_PCT"])
    df.set_value(index, "TS_PCT", temp_row["TS_PCT"])
    df.set_value(index, "USG_PCT", temp_row["USG_PCT"])
    df.set_value(index, "PACE", temp_row["PACE"])
    df.set_value(index, "PIE", temp_row["PIE"])
    #print( df.head() )
    #break

df.to_sql("modified_gamelogs", conn, if_exists='replace')
