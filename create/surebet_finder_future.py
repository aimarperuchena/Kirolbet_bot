import urllib.request
import pymysql
import urlopen
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime
from datetime import date
import pymysql.cursors
dbServerName = "81.25.126.97"
dbUser = "remote"
dbPassword = "kirolBet20a"
dbName = "Kirolbet_db"

connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                             db=dbName)
def selectGames(sport_id):
    result=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "select game.id as game_id, league.id as league_id, sport.id as sport_id, game.game as game_des from game, sport, league where sport.id=game.sport_id and league.id=game.league_id and game.sport_id=%s and game.date>=now(); "
            cursor.execute(sql, (sport_id))
            result=cursor.fetchall()
    except Exception as e:
        print('SELECT GAMES')
        print(e)
        

    finally:
        return result

def selectMarkets(sport_id):
    result=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM Kirolbet_db.market where sport_id=%s limit 25; "
            cursor.execute(sql, (sport_id))
            result=cursor.fetchall()
    except Exception as e:
        print('SELECT MARKETS')
        print(e)
        

    finally:
        return result
def selectGameBets(game_id, market_id):
    result=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "select game_bet.id, game_bet.market_id, market.des from game_bet, market where market.id=game_bet.market_id and game_bet.game_id=%s and game_bet.market_id= %s;  "
            cursor.execute(sql, (game_id, market_id))
            result=cursor.fetchall()
    except Exception as e:
        print('SELECT GAME BETS')
        print(e)
        

    finally:
        return result

def selectSports():
    result=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "select * from sport "
            cursor.execute(sql, ())
            result=cursor.fetchall()
    except Exception as e:
        print('SELECT SPORTS')
        print(e)
        

    finally:
        return result
def selectMaxOdds(game_bet, des):
    result=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT id, odd FROM Kirolbet_db.odds where game_bet_id=%s and des like %s order by odd desc limit 1; "
            cursor.execute(sql, (game_bet, des))
            result=cursor.fetchone()
    except Exception as e:
        print('SELECT MAX ODDS')
        print(e)
    finally:
        return result
def selectOddOptions(game_bet):
    result=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT distinct des FROM odds where game_bet_id=%s ; "
            cursor.execute(sql, (game_bet))
            result=cursor.fetchall()
    except Exception as e:
        print('SELECT ODD OPTIONS')
        print(e)
    finally:
        return result

def insertSurebet(game_id, market_id, league_id, sport_id, game_bet_id, benefit):
    row_id = ''

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `surebet` (`game_id`, `market_id`, `sport_id`,`league_id`,`game_bet_id`,`benefit`) VALUES (%s, %s,%s,%s,%s,%s)"
            cursor.execute(sql, (game_id, market_id, sport_id, league_id, game_bet_id, benefit))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid

    except Exception as e:
        print('INSERT SUREBET')
        print(e)
       

    finally:

        return row_id

def insertSurebetOdd(surebet_id, odd_id):
    row_id = ''

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `surebet_odd` (`odd_id`, `surebet_id`) VALUES (%s, %s)"
            cursor.execute(sql, (odd_id, surebet_id))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid

    except Exception as e:
        print('INSERT SUREBET_ODD')
        print(e)
       

    finally:

        return row_id

def selectSurebet(game_id, game_bet_id, sport_id, benefit):
    result=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT *  FROM surebet where game_id=%s and game_bet_id=%s and sport_id=%s and benefit=%s "
            cursor.execute(sql, (game_id, game_bet_id, sport_id, benefit))
            result=cursor.fetchall()
    except Exception as e:
        print('SELECT ODD OPTIONS')
        print(e)
    finally:
        return result
def main():
    sports=selectSports()
    for sport in sports:
        sport_id=sport[0]
        games=''
        game_bets=''
        '''SELECT GAMES'''
        games=selectGames(sport_id)
    
        for game in games:
            game_id=game[0]
            league_id=game[1]
            
            game_des=game[3]
            markets=selectMarkets(sport_id)
            market_array=[]
            for market in markets:
                market_id=market[0]
           
                game_bets=selectGameBets(game_id,market_id)
                for game_bet in game_bets:
                    
                    game_bet_id=game_bet[0]
                    market_id=game_bet[1]
                    market_des=game_bet[2]
                    surebet=0
                    options=selectOddOptions(game_bet_id)
                    for option in options:
                    
                        odd=selectMaxOdds(game_bet_id,option[0])
                        surebet=surebet+(1/odd[1])
                    if(surebet<1):
                        surebet=1-surebet
                        surebet=surebet*100
                        surebet_exist=selectSurebet(game_id,game_bet_id, sport_id, surebet)
                        print(len(surebet_exist))
                        if(len(surebet_exist)==0):
                            surebet_id=insertSurebet(game_id, market_id, league_id, sport_id, game_bet_id,surebet)
                            options=selectOddOptions(game_bet_id)
                            for option in options:
                            
                                odd=selectMaxOdds(game_bet_id,option[0])
                                odd_id=odd[0]
                                insertSurebetOdd(surebet_id, odd[0])
                            print(game_des+' '+market_des+' '+str(surebet))
                            


                        
                        
                    


        
a = 1
while a == 1:
    print('NEW SCANN')
    main()
    time.sleep(43200)
