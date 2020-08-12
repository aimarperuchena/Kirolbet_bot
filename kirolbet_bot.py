
import urllib.request
import pymysql
import urlopen
import request
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime

from bs4 import BeautifulSoup

import requests


def extract_odds(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = link
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)

    lista_apuestas = soup2.find("ul", {"class": "apuestas"})

    row_apuestas = lista_apuestas.findAll("li", {"class": "filtroCategoria"})
    for row in row_apuestas:
        time.sleep(1)
        error = False
        odd_1 = ''
        odd_x = ''
        odd_2 = ''
        team_1 = ''
        team_2 = ''
        timestamp = ''
        league = ''
        try:
            '''MATCH INFO (TIME TEAMS)'''
            info_partido = row.find("div", {"class": "infoEve"})
            info_div = info_partido.find("div", {"class": "info"})

            '''TEAMS NAME'''
            partido_div = info_div.find("span", {"class": "partido"})
            text = partido_div.text
            text = text.split('(')
            match = text[0]
            teams_array = match.split('vs')
            team_1 = teams_array[0]
            team_2 = teams_array[1]

            '''LEAGUE'''
            league_div = info_div.find('span', {"class": "overStar"})
            league_span = league_div.find("span", {"class": "campeonato"})
            league = league_span.text
            '''MATCH ODDS GENERAL DIV'''
            apuestas_div = row.find("div", {"class": "apuestas_fut"})
            timestamp = apuestas_div['dt']

            market_1x2_div = apuestas_div.find('ul', {"des": "1X2"})

            '''MARKET 1 ODDS'''

            '''ODD 1'''
            market_1_a = market_1x2_div.find('a', {"title": "1"})
            odd_1_span = market_1_a.find('span', {"class": "coef"})
            odd_1 = odd_1_span.text

            '''ODD X'''
            market_x_a = market_1x2_div.find('a', {"title": "X"})
            odd_x_span = market_1_a.find('span', {"class": "coef"})
            odd_x = odd_x_span.text

            '''ODD 2'''
            market_2_a = market_1x2_div.find('a', {"title": "2"})
            odd_2_span = market_2_a.find('span', {"class": "coef"})
            odd_2 = odd_2_span.text

            if error == False:
                team_2 = team_2.replace(".", "")
                team_2 = team_2.strip()
                team_1 = team_1.strip()
                league = league.strip()

                print('LEAGUE: ' + league)
                print(team_1+': '+odd_1)
                print('X : '+odd_x)
                print(team_2+': '+odd_2)
                print(timestamp)
                print('---------------------')
                timestamp = timestamp.replace("/", "-")
                game = team_1 + ' - '+team_2
                url = 'http://localhost:3000/api/odds'
                myobj = {'game': game, 'timestamp': timestamp, 'league': league, 'team_1': team_1,
                         'team_2': team_2, 'bookie': 'Kirolbet', 'market': '1X2', 'odds': [odd_1, odd_x, odd_2], 'options':["1","X","2"]}

                x = requests.post(url, data=myobj)
                print(x)

        except Exception as e:
            print(e)
            error = True


with open('kirolbet_ligas_futbol.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'html')

    general_ul = soup.find("ul", {"class": "ksAccordion-toggle"})
    li_array = general_ul.findAll("li")
    print(len(li_array))
    for row in li_array:

        div_section = row.find("div", {"class": "seccion"})
        a_section = div_section.find("a")
        link = 'https://euskadi.kirolbet.es'+a_section['href']
        print(link)
        extract_odds(link)
