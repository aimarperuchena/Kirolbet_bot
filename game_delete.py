import urllib.request
import pymysql
import urlopen
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime
from datetime import date
import pymysql.cursors
dbServerName = "188.166.163.174"
dbUser = "remote"
dbPassword = "aimar"
dbName = "Kirolbet_db"

connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                             db=dbName)




def selectGame(game):
    
    res=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id` FROM `game` WHERE `game`=%s "
            cursor.execute(sql, (game))
            result = cursor.fetchall()
            res=result
    except Exception as e:
        print('SELECT GAME')
        print(e)

    finally:

        return res



def deleteGameBet(game_bet):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from game_bet where id = %s"
            cursor.execute(sql, (game_bet))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            
    except Exception as e:
        print('DETE gamebet ERROR')   
def deleteGame(game):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from game where id = %s"
            cursor.execute(sql, (game))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

    except Exception as e:
        print('DETE game ERROR')  
        print(e)
def deleteGameTeam(game_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from game_team where game_id = %s"
            cursor.execute(sql, (game_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

    except Exception as e:
        print('DETE game ERROR')  
        print(e)  
def selectGameBet(game_id):
    game_bet = ''

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id` FROM `game_bet` WHERE `game_id`=%s"
            cursor.execute(sql, (game_id))
            result = cursor.fetchall()
            game_bet=result
    except Exception as e:
       
        print(e)
        

    finally:

        return game_bet


def deleteOdds(game_bet):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from odds where game_bet_id = %s"
            cursor.execute(sql, (game_bet))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
           
    except Exception as e:
        print('DETE ODDS ERROR')


def selectMultipleGames():
    res=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "select count(*) as tot, game.game from game  group by game.game HAVING tot > 1 order by tot desc ;"
            cursor.execute(sql)
            result = cursor.fetchall()
            res=result
    except Exception as e:
        print('SELECT GAMES REPEATED')
        print(e)

    finally:

        return res
def main():
    repeated_games=selectMultipleGames()
    print(repeated_games[0])
    for repeated in repeated_games:
        game_des=repeated[1]
        games=selectGame(game_des)
        for game in games:

            game_id=game[0]

            game_bets=selectGameBet(game_id)
            for game_bet in game_bets:
                game_bet_id=game_bet[0]
                deleteOdds(game_bet_id)
                deleteGameBet(game_bet_id)
            deleteGameTeam(game_id)
            deleteGame(game_id)

main()