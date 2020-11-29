
import urllib.request
import pymysql
import urlopen
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime
from datetime import date
import pymysql.cursors
import sys
dbServerName = "81.25.126.97"
dbUser = "remote"
dbPassword = "kirolBet20a"
dbName = "Kirolbet_db"

connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                             db=dbName)
def extractMatchList(link, i):
    cont=0
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        reg_url = link
        req = Request(url=reg_url, headers=headers)
        html = urlopen(req).read()
        soup2 = BeautifulSoup(html,  "html.parser")
        games = soup2.findAll("li", {"class": "filtroCategoria"})
        cont=len(games)
        print(str(i)+': '+str(cont))
        return cont
    except Exception as e:
        print(e)
        return 0
    
def insertLeague(link, state):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `league_link` (`des`, `state`) VALUES (%s, %s)"
            cursor.execute(sql, (link, str(state)))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            row_id = cursor.lastrowid

    except Exception as e:
        print(e)
        


    

def selectLeague(link):
    res=''
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `des`,`state` FROM `league_link` WHERE `link`=%s "
            cursor.execute(sql, (link))
            res = cursor.fetchone()
            return res
    except Exception as e:
        print(e)
    finally:
        return res
cont=1
for x in range(1, 6300):
    link = 'https://euskadi.kirolbet.es/esp/Sport/Competicion/'+str(x)
    val=extractMatchList(link,x)
    state='a'
    if(val>0):
        state=1
    else:
        state=0
    """ select_result=selectLeague(link) """
    insertLeague(link, state)
