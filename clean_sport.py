import pymysql.cursors
dbServerName = "35.242.242.84"
dbUser = "remote"
dbPassword = "aimar"
dbName = "Kirolbet_db"


connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                             db=dbName)
def selectGames(sport_id):
    games = ''

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id` FROM `game` WHERE `sport_id`=%s"
            cursor.execute(sql, (sport_id))
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
def deleteLeagues(sport_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from league where sport_id = %s"
            cursor.execute(sql, (sport_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

    except Exception as e:
        print('DETE league ERROR')  
        print(e)  
def deleteSport(sport_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from sport where id = %s"
            cursor.execute(sql, (sport_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

    except Exception as e:
        print('DETE sport ERROR')  
        print(e)  

def deleteMarkets(sport_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from market where sport_id = %s"
            cursor.execute(sql, (sport_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

    except Exception as e:
        print('DETE market ERROR')  
        print(e) 
def deleteTeam(sport_id):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "Delete from team where sport_id = %s"
            cursor.execute(sql, (sport_id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

    except Exception as e:
        print('DETE team ERROR')  
        print(e)    
def main(sport_id):
    games=selectGames(sport_id)
    for game in games:
        game_id=game[0]
        game_bets=selectGameBet(game_id)
        for game_bet in game_bets:
            game_bet_id=game_bet[0]
            deleteOdds(game_bet_id)
            deleteGameBet(game_bet_id)
        deleteGameTeam(game_id)
        deleteGame(game_id)
    deleteLeagues(sport_id) 
    deleteMarkets(sport_id) 
    deleteTeam(sport_id) 
       


main(3)
