import pandas as pd
import sqlite3

predictions = pd.read_excel(open('project/final_table_machine_learning_NBA_data.xlsx','rb'), sheetname='Sheet1')
conn = sqlite3.connect('project/nba.db')
player_info = pd.read_sql_query("select * from players_common_info", conn)
newdf = predictions.tail(1)
df1 = newdf.ix[:,2:]

def get_position( player_id ):
    info = player_info[player_info["PERSON_ID"] == player_id]["POSITION"]
    if info.iloc[0] != '':
        return info.iloc[0][0]
    else:
        return ""

results = []
temp = []
max_score = -1
score = 0
hash = {"G": 4, "F": 4, "C": 1}

def DFS(idx):
    global results, temp, max_score, score, hash
    if len(results) == 10 and hash["G"] + hash["F"] + hash["C"] == 0:
        if max_score < score:
            max_score = score
            results = temp
        return

    for column in df1.iloc[:,idx:]:
        ##get player position
        pos = get_position(column)
        if pos == '' or hash[pos] == 0:
            idx += 1
            continue
        print (column)
        hash[pos] -= 1
        temp.append(column)
        if df1[column].iloc[0] != -9999:
            score += df1[column].iloc[0]
        DFS(idx+1)
        temp.remove(column)
        if df1[column].iloc[0] != -9999:
            score -= df1[column].iloc[0]
        hash[pos] += 1

DFS(0)

print (results)
