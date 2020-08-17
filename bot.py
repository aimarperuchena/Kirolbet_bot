

import mysql.connector

import time

from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen
import datetime
import sys

import requests
import ssl

# This restores the same behavior as before.


dbServerName = "us-cdbr-east-02.cleardb.com"
dbUser = "b2070edf1025c4"
dbPassword = "ad65023d"
dbName = "heroku_148a4f741dd1947"


def insertMarket(market, sport):
    """  mydb = mysql.connector.connect(
        host=dbServerName, user=dbUser, password=dbPassword,
        db=dbName
    )

    mycursor = mydb.cursor()

    ''' Create a new record'''
    sql = "INSERT INTO `market` (`sport`, `des`) VALUES (%s, %s)"
    mycursor.execute(sql, (sport, market)
    a=mycursor.lastrowid """
    try:
        mydb = mysql.connector.connect(
            host=dbServerName, user=dbUser, password=dbPassword,
            db=dbName
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO `market` (`sport`, `des`) VALUES (%s, %s)"

        mycursor.execute(sql,  (sport, market))

        mydb.commit()
        row_id = mycursor.lastrowid
        return row_id
    except Exception as e: 
        
        print(e)


def selectMarket(market, sport):
    market_id = ''
    """  connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                 db=dbName
                                 )
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
        connection.close()
        return market_id """
    try:    
        mydb = mysql.connector.connect(
            host=dbServerName, user=dbUser, password=dbPassword,
            db=dbName
        )

        mycursor = mydb.cursor()

        sql = "SELECT `id` FROM `market` WHERE `sport`=%s AND `des`=%s"
        mycursor.execute(sql, (sport, market))

        result = mycursor.fetchone()
        if result == None:

            market_id = insertMarket(market, sport)
        else:
            market_id = result[0]
        return market_id
    except Exception as e:
        
        print(e)


def insertGame(sport, league, game, date, times):
    row_id = ''
    """ connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                 db=dbName)
    row_id = ''

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `game` (`game`, `date`, `time`,`sport`,`league`) VALUES (%s, %s,%s,%s,%s)"
            cursor.execute(sql, (game, date, times, sport, league))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid

    except ValueError as e:
        print('Value error')

    finally:
        connection.close()
        return row_id
 """
    try:
        mydb = mysql.connector.connect(
            host=dbServerName, user=dbUser, password=dbPassword,
            db=dbName
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO `game` (`game`, `date`, `time`,`sport`,`league`) VALUES (%s, %s,%s,%s,%s)"
        mycursor.execute(sql, (game, date, times, sport, league))

        mydb.commit()
        row_id = mycursor.lastrowid
        return row_id
    except Exception as e: 
        
        print(e)


def selectGame(sport, league, game, date, times):
    game_id = ''
    """ connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                 db=dbName
                                 )
    game_id = ''
    try:

        with connection.cursor() as cursor:

            # Read a single record
            sql = "SELECT `id` FROM `game` WHERE `sport`=%s AND `date`=%s AND `time`=%s AND `league`=%s AND `game`=%s"
            cursor.execute(sql, (sport, date, times, league, game))
            result = cursor.fetchone()
            if result == None:

                game_id = insertGame(sport, league, game, date, times)
            else:
                game_id = result[0]

    finally:
        connection.close()
        return game_id """
    try:
        mydb = mysql.connector.connect(
            host=dbServerName, user=dbUser, password=dbPassword,
            db=dbName
        )

        mycursor = mydb.cursor()

        sql = "SELECT `id` FROM `game` WHERE `sport`=%s AND `date`=%s AND `time`=%s AND `league`=%s AND `game`=%s"
        mycursor.execute(sql, (sport, date, times, league, game))
        result = mycursor.fetchone()
        if result == None:

            game_id = insertGame(sport, league, game, date, times)
        else:
            game_id = result[0]
        return game_id
    except Exception as e:
        
        print(e)

def insertGameBet(game_id, market_id):
    """ connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                 db=dbName)
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
        connection.close()
        return row_id """
    try:    
        mydb = mysql.connector.connect(
            host=dbServerName, user=dbUser, password=dbPassword,
            db=dbName
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO `game_bet` (`game_id`, `market_id`) VALUES (%s, %s)"
        mycursor.execute(sql, (game_id, market_id))

        mydb.commit()
        row_id = mycursor.lastrowid
        return row_id
    except Exception as e: 
        
        print(e)

def selectGameBet(game_id, market_id):
    """ connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                 db=dbName
                                 )
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
        connection.close()
        return game_bet_id
 """
    try:
        game_bet_id = ''
        mydb = mysql.connector.connect(
            host=dbServerName, user=dbUser, password=dbPassword,
            db=dbName
        )

        mycursor = mydb.cursor()

        sql = "SELECT `id` FROM `game_bet` WHERE `game_id`=%s AND `market_id`=%s "
        mycursor.execute(sql, (game_id, market_id))
        result = mycursor.fetchone()
        if result == None:
            game_bet_id = insertGameBet(game_id, market_id)
        else:
            game_bet_id = result[0]
        return game_bet_id
    except Exception as e: 
        
        print(e)

def insertOdd(game_bet_id, des, odd):
    
    """ connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                 db=dbName)
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
        connection.close()
        return row_id """
    try:
        mydb = mysql.connector.connect(
            host=dbServerName, user=dbUser, password=dbPassword,
            db=dbName
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO `odds` (`game_bet_id`, `des`,`odd`) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (game_bet_id, des, odd))

        mydb.commit()
        row_id = mycursor.lastrowid
        return row_id
    except Exception as e: 
        
        print(e)

def selectOdd(game_bet_id, des, odd):
    """ connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                 db=dbName
                                 )

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
        connection.close() """
    try:    
        mydb = mysql.connector.connect(
            host=dbServerName, user=dbUser, password=dbPassword,
            db=dbName
        )

        mycursor = mydb.cursor()

        sql = "SELECT `id`, `odd` FROM `odds` WHERE `game_bet_id`=%s AND `des`=%s  ORDER BY `created_at` DESC "
        mycursor.execute(sql, (game_bet_id, des))
        result = mycursor.fetchone()
        if result == None:
            insertOdd(game_bet_id, des, odd)

        else:
            if float(result[1]) != float(odd):
                insertOdd(game_bet_id, des, odd)
    except Exception as e: 
        
        print(e)

def extractMatchList(link):
    """   agent={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    
    reg_url = link
    context = ssl._create_unverified_context()
    req = Request(url=reg_url, headers=agent)
    html = urlopen(req,context=context).read() """
    print('GAMEEEEEEEEEEEEE')
    try:
        html = requests.get(link)

        soup2 = BeautifulSoup(html.content,  "html.parser")
        games = soup2.findAll("li", {"class": "filtroCategoria"})
        print('aaaaaa')
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
    except Exception as e: 
       
        print(e)


def extractMarkets(link):
    try:
        """ agent={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                          'AppleWebKit/537.11 (KHTML, like Gecko) '
                          'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}

        reg_url = link
        context = ssl._create_unverified_context()
        req = Request(url=reg_url, headers=agent)
        html = urlopen(req,context=context).read() """
        print('MARKETSSSSSSSSSS')
        html=requests.get(link)
        soup2 = BeautifulSoup(html.content, "html.parser")

        date_time = ''
        date = ''
        times = ''
        game = ''
        game_id = ''
        market_id = ''

        sport = ''
        league = ''

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

        '''SELECT GAME DB'''
        print(game)
        
        game_id = selectGame(sport, league, game, date, times)
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
    except Exception as e: 
        
        print(e)

def extractLeagues():
    with open('ligas.html', 'r') as f:
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
    try: 
        print('new scann')
        
        extractLeagues()
        time.sleep(900)
    except Exception as e: 
        
        print(e)
''' extractMarkets("https://euskadi.kirolbet.es/esp/Sport/Evento/2148667")
 '''
