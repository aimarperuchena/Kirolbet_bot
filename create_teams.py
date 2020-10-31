import urllib.request
import pymysql
import urlopen
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime


import pymysql.cursors
dbServerName = "188.166.163.174"
dbUser = "remote"
dbPassword = "aimar"
dbName = "Kirolbet_db"

connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                             db=dbName)

def selectGames():
    a=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `game`,`id`, `league_id`, `sport_id` FROM `game` WHERE `teams_created`='0'"
            cursor.execute(sql)
            result = cursor.fetchall()
            
            a=result
    except Exception as e: 
        print('SELECT GAMES')
        print(e)
    finally:
        return a

def insertTeam(des, sport_id):
    row_id = ''

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `team` (`des`, `sport_id`) VALUES ( %s,%s)"
            cursor.execute(sql, (des, sport_id))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid
    except Exception as e:
        print('INSERT TEAM')
        print(e)
        


    finally:

        return row_id
def selectTeam(des, sport_id):
    row_id=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id` FROM `team` WHERE `sport_id`=%s and `des` like %s"
            cursor.execute(sql, (sport_id, des))
            result = cursor.fetchone()
           
            if result == None:
                
                row_id = insertTeam(des, sport_id)

            else:
                row_id = result[0]
           
    except Exception as e: 
        print('SELECT TEAM')
        print(e)
    finally:
        return row_id  
 
def insertGameTeam(game_id, team_id,league_id):
    row_id = ''

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `game_team` (`game_id`, `team_id`,`league_id`) VALUES ( %s,%s, %s)"
            cursor.execute(sql, (game_id, team_id,league_id))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid
    except Exception as e:
        print('INSERT GAME TEAM')
        print(e)
        


    finally:

        return row_id
def selectGameTeam(game_id, team_id, league_id):
    row_id=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id` FROM `game_team` WHERE `game_id`=%s and `team_id`=%s"
            cursor.execute(sql, (game_id, team_id))
            result = cursor.fetchone()
           
            if result == None:
                
                row_id = insertGameTeam(game_id, team_id,league_id)

            else:
                row_id = result[0]
           
    except Exception as e: 
        print('SELECT GAME TEAM')
        print(e)
    finally:
        return row_id 

def updateGame(game_id):
    try:

        with connection.cursor() as cursor:

            # Read a single record
            sql = "UPDATE game set teams_created = %s where id=%s"
            cursor.execute(sql, ('1', game_id))
            result = cursor.fetchone()
    except Exception as e: 
        print('UPDATE GAME')
        print(e)   
   
    finally:

        return result
def main():
    games=selectGames()
    for game in games:
        game_id=game[1]
        game_des=game[0]
        league_id=game[2]
        sport_id=game[3]
        game_split=game_des.strip().split("vs.")
        for team in game_split:
            team=team.strip()
            '''SELECT THE TEAM_ID'''
            team_id=selectTeam(team,sport_id)
            selectGameTeam(game_id,team_id, league_id)
            '''SELECT GAMES WHERE THE TEAM NAME EXIST'''
        updateGame(game_id)
main()