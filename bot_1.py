import urllib.request
import pymysql
import urlopen
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime


import requests
import pymysql.cursors
dbServerName = "35.242.242.84"
dbUser = "remote"
dbPassword = "aimar"
dbName = "Kirolbet_db"

connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                             db=dbName)


def insertMarket(market, sport):

    row_id = ''
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `market` (`sport`, `des`) VALUES (%s, %s)"
            cursor.execute(sql, (sport, market))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid

    finally:

        return row_id


def selectMarket(market, sport):
    market_id = ''

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id` FROM `market` WHERE `sport`=%s AND `des`=%s"
            cursor.execute(sql, (sport, market))
            result = cursor.fetchone()
            if result == None:

                market_id = insertMarket(market, sport)
            else:
                market_id = result[0]

    finally:

        return market_id


def insertGame(sport_id, league_id, game, date, times):

    row_id = ''

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `game` (`game`, `date`, `time`,`sport_id`,`league_id`) VALUES (%s, %s,%s,%s,%s)"
            cursor.execute(sql, (game, date, times, sport_id, league_id))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid

    except ValueError as e:
        print('Value error')

    finally:

        return row_id


def selectGame(sport_id, league_id, game, date, times):

    game_id = ''
    try:

        with connection.cursor() as cursor:

            # Read a single record
            sql = "SELECT `id` FROM `game` WHERE `sport_id`=%s AND `date`=%s AND `time`=%s AND `league_id`=%s AND `game`=%s"
            cursor.execute(sql, (sport_id, date, times, league_id, game))
            result = cursor.fetchone()
            if result == None:

                game_id = insertGame(sport_id, league_id, game, date, times)
            else:
                game_id = result[0]

    finally:

        return game_id


def insertGameBet(game_id, market_id):

    row_id = ''

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `game_bet` (`game_id`, `market_id`) VALUES (%s, %s)"
            cursor.execute(sql, (game_id, market_id))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid
    except ValueError as e:
        print('Value error')

    finally:

        return row_id


def selectGameBet(game_id, market_id):

    game_bet_id = ''
    try:

        with connection.cursor() as cursor:

            # Read a single record
            sql = "SELECT `id` FROM `game_bet` WHERE `game_id`=%s AND `market_id`=%s "
            cursor.execute(sql, (game_id, market_id))
            result = cursor.fetchone()
            if result == None:

                game_bet_id = insertGameBet(game_id, market_id)
            else:
                game_bet_id = result[0]

    finally:

        return game_bet_id


def insertOdd(game_bet_id, des, odd):
    row_id = ''

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `odds` (`game_bet_id`, `des`,`odd`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (game_bet_id, des, odd))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
    except ValueError as e:
        print('Value error')

    finally:

        return row_id


def selectOdd(game_bet_id, des, odd):

    try:

        with connection.cursor() as cursor:

            # Read a single record
            sql = "SELECT `id`, `odd` FROM `odds` WHERE `game_bet_id`=%s AND `des`=%s  ORDER BY `created_at` DESC "
            cursor.execute(sql, (game_bet_id, des))
            result = cursor.fetchone()
            if result == None:
                insertOdd(game_bet_id, des, odd)

            else:
                if float(result[1]) != float(odd):
                    insertOdd(game_bet_id, des, odd)
    finally:
        d = 1


def selectSport(des):
    row_id = 0
    try:

        with connection.cursor() as cursor:

            # Read a single record
            sql = "SELECT `id` FROM `sport` WHERE `des`=%s "
            cursor.execute(sql, (des))
            result = cursor.fetchone()
            if result == None:
                row_id = insertSport(des)

            else:
                row_id = result[0]
    except Exception as e: print(e)
    finally:
        return row_id


def insertSport(des):
    row_id = ''

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `sport` (`des`) VALUES ( %s)"
            cursor.execute(sql, (des))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid
    except ValueError as e:
        print('Value error')

    finally:

        return row_id


def selectLeague(sport_id, des):
    row_id = ''
    try:

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id` FROM `league` WHERE `des`=%s AND `sport_id`=%s "
            cursor.execute(sql, (des, sport_id))
            result = cursor.fetchone()
            if result == None:
                
                row_id = insertLeague(sport_id, des)

            else:
                row_id = result[0]
    except Exception as e:
        print('aaaaa'+e)
    finally:
        return row_id


def insertLeague(sport_id, des):
    row_id = ''

    try:
        with connection.cursor() as cursor:
           
            # Create a new record
            sql = "INSERT INTO `league` (`des`, `sport_id`) VALUES ( %s, %s)"
            cursor.execute(sql, (des, sport_id))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid
    except Exception as e:
      
        print(e)

    finally:

        return row_id


def extractMatchList(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = link
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html,  "html.parser")
    games = soup2.findAll("li", {"class": "filtroCategoria"})
    for game in games:
        game_info = game.find("div", {"class": "infoEve"})
        info = game_info.find("div", {"class": "info"})

        '''GAME LEAGUE'''

        overStar = info.find("span", {"class": "overStar"})
        span_campeonato = overStar.find("span", {"class": "campeonato"})
        league = span_campeonato.text

        '''GAME LINK AND TITLE'''
        span_game = info.find("span", {"class": "partido"})
        a_array = span_game.findAll("a")
        if(len(a_array) == 1):
            game_a = a_array[0]
        else:
            game_a = a_array[1]

        '''GAME LINK'''
        game_link = game_a['href']
        link = 'https://euskadi.kirolbet.es'+game_link
        extractMarkets(link)
        time.sleep(0.1)


def extractMarkets(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = link
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html, "html.parser")

    date_time = ''
    date = ''
    times = ''
    game = ''
    game_id = ''
    market_id = ''
    sport_id = ''
    sport = ''
    league = ''
    league_id = ''

    '''DATE'''
    span_date = soup2.find("span", {"class": "hora dateFecha"})
    date_time = span_date['title']
    date_time = date_time.split(" ")
    date = date_time[0]
    times = date_time[1]
    times = times.replace("Z", "")

    '''GAME TEAMS'''
    game_title = soup2.find("h3", {"class": "titulo_seccion"})
    game = game_title.text

    '''SPORT'''
    div_breadcrumb = soup2.find("div", {"class": "breadcrumb"})
    ul_breadcrumb = div_breadcrumb.find("ul")
    lis_breadcrumb = ul_breadcrumb.findAll("li")
    sport = lis_breadcrumb[1].text.strip()
    league = lis_breadcrumb[2].text
    sport_id = selectSport(sport)
   
    league_id = selectLeague(sport_id, league)

    '''SELECT GAME DB'''
    game_id = selectGame(sport_id, league_id, game, date, times)
    '''MARKETS'''
    next_markets = soup2.find("div", {"class": "prox_eventos"})
    markets = next_markets.findAll(
        "ul", {"market-group-id": "market.MarketGroupId"})
    ''' game_info = [{"date": date}, {"game": game},
                 {"sport": sport}, {"league": league}] '''

    markets_array = []
    for market in markets:
        market_id = ''
        game_bet_id = ''
        market_des = market["des"].strip()
        market_id = selectMarket(market_des, sport)
        odds_toggle = market.find("li", {"class": "ksToggle"})
        market_odds_div = odds_toggle.find(
            "div", {"class": "apuestas_partido"})
        market_odds_a = market_odds_div.findAll("a")

        odds_array = []
        game_bet_id = selectGameBet(game_id, market_id)
        for odd_a in market_odds_a:
            des = odd_a["des"]
            coef = odd_a.find("span", {"class": "coef"})
            odd = coef.text.replace(",", ".")
            selectOdd(game_bet_id, des, odd)
    print(league+' -- '+game)


def extractLeagues():
    with open('ligas_1.html', 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents,  "html.parser")
        general_ul = soup.find("ul", {"class": "ksAccordion-toggle"})
        li_array = general_ul.findAll("li")

        for row in li_array:

            div_section = row.find("div", {"class": "seccion"})
            a_section = div_section.find("a")
            link = 'https://euskadi.kirolbet.es'+a_section['href']
            extractMatchList(link)


a = 1
while a == 1:
    print('new scann')
    try:
        extractLeagues()
    except Exception as e:
        print(e)
    
    time.sleep(300)
