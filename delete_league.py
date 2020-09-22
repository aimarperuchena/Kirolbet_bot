import pymysql.cursors
dbServerName = "35.242.242.84"
dbUser = "remote"
dbPassword = "aimar"
dbName = "Kirolbet_db"


connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                             db=dbName)



def selectGames(league_id):
    games = ''

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id` FROM `game` WHERE `league_id`=%s"
            cursor.execute(sql, (league_id))
            result = cursor.fetchall()
            games=result
    except Exception as e:
       
        print(e)
        

    finally:

        return games
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

def deleteLeague(league_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from league where id = %s"
            cursor.execute(sql, (league_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

    except Exception as e:
        print('DETE league ERROR')  
        print(e) 

def main(league_id):
    games=selectGames(league_id)
    print(games)
    for game in games:
        game_id=game[0]
        
        game_bets=selectGameBet(game_id)
        for game_bet in game_bets:
            game_bet_id=game_bet[0]
            deleteOdds(game_bet_id)
            deleteGameBet(game_bet_id)
        deleteGameTeam(game_id)
        deleteGame(game_id)
    deleteLeague(league_id)
try:
    main(14)
   
except Exception as e:
    print(e)

    
