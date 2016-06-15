import sqlite3

conn = sqlite3.connect('nba.db')
c = conn.cursor()

c.execute('''CREATE TABLE gamelogs (SEASON_ID text, 
	                               PLAYER_ID integer,
	                               PLAYER_NAME text,
	                               TEAM_ABBREVIATION text,
	                               TEAM_NAME text,
	                               GAME_ID text,
	                               GAME_DATE text,
	                               MATCHUP text,
	                               WL text,
	                               MIN integer,
	                               FGM integer,
	                               FGA integer,
	                               FG_PCT integer,
	                               FG3M integer,
	                               FG3A integer,
	                               FG3_PCT integer,
	                               FTM integer,
	                               FTA integer,
	                               FT_PCT integer,
	                               OREB integer,
	                               DREB integer,
	                               REB integer,
	                               AST integer,
	                               STL integer,
	                               BLK integer,
	                               TOV integer,
	                               PF integer,
	                               PTS integer,
	                               PLUS_MINUS integer,
	                               VIDEO_AVAILABLE integer)''')

f = open('gamelogs.txt', 'r')
gamelogs = f.readlines()

for gamelog in gamelogs:
	log = eval(gamelog)
	print (log)
	c.execute('INSERT INTO gamelogs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', 
		log)

conn.commit()
conn.close()