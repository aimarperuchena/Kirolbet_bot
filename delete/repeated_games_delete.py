import urllib.request
import pymysql
import urlopen
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime
from datetime import date
import pymysql.cursors
dbServerName = "localhost"
dbUser = "user"
dbPassword = "password"
dbName = "database"

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
        print('DETE gamebet ERROR ') 
        print(e) 

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
        print('DETE ODDS ERROR ')
        print(e)


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
def deleteSurebetOdds(surebet_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from surebet_odd where surebet_id = %s"
            cursor.execute(sql, (surebet_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
           
    except Exception as e:
        print('DELETE SUREBET_ODD ERROR ')
        print(e)
def deleteSurebet(game_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from surebet where game_id = %s"
            cursor.execute(sql, (game_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
           
    except Exception as e:
        print('DELETE SUREBET ERROR ')
        print(e)
def selectGameBetSurebets(game_bet_id):
    res=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "select `id` from surebet  where game_bet_id=%s;"
            cursor.execute(sql,(game_bet_id))
            result = cursor.fetchall()
            res=result
    except Exception as e:
        print('SELECT SUREBETS')
        print(e)

    finally:

        return res

def deleteGameGameBets(game_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from game_bet where game_id = %s"
            cursor.execute(sql, (game_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
           
    except Exception as e:
        print('DELETE GAME GAMEBETS ERROR ')
        print(e)
def deleteGameSurebets(game_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from surebet where game_id = %s"
            cursor.execute(sql, (game_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
           
    except Exception as e:
        print('DELETE GAME SUREBETS ERROR ')
        print(e)
def main():
    repeated_games=selectMultipleGames()
    for repeated in repeated_games:
        game_des=repeated[1]
        print(game_des)
        games=selectGame(game_des)
        for game in games:

            game_id=game[0]
            game_bets=selectGameBet(game_id)
            for game_bet in game_bets:
                game_bet_id=game_bet[0]
                surebets=selectGameBetSurebets(game_bet_id)
                for surebet in surebets:
                    surebet_id=surebet[0]
                    deleteSurebetOdds(surebet_id)
                    
                deleteOdds(game_bet_id)
            deleteGameSurebets(game_id)
            deleteGameGameBets(game_id)  
              
            deleteGameTeam(game_id)
            deleteGame(game_id)

a = 1
while a == 1:
    print('NEW SCAN')
    main()
    time.sleep(86400)