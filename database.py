import sqlite3

conn = sqlite3.connect('nba.db')
c = conn.cursor()

c.execute('''CREATE TABLE players (PERSON_ID integer, 
	                               DISPLAY_LAST_COMMA_FIRST text,
	                               DISPLAY_FIRST_LAST text,
	                               ROSTERSTATUS integer,
	                               FROM_YEAR text,
	                               TO_YEAR text,
	                               PLAYERCODE text,
	                               TEAM_ID integer,
	                               TEAM_CITY text,
	                               TEAM_NAME text,
	                               TEAM_ABBREVIATION text,
	                               TEAM_CODE text,
	                               GAMES_PLAYED_FLAG text)''')

f = open('test.txt', 'r')
players = f.readlines()

for player in players:
	pl = eval(player)
	print (pl)
	c.execute('INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', 
		pl)

conn.commit()
conn.close()