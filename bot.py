
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


def extractMatchList(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = link
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)
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
    soup2 = BeautifulSoup(html)

    date = ''
    game = ''
    team_1 = ''
    team_2 = ''
    sport = ''
    league = ''

    '''DATE'''
    span_date = soup2.find("span", {"class": "hora dateFecha"})
    date = span_date["title"]

    '''GAME TEAMS'''
    game_title = soup2.find("h3", {"class": "titulo_seccion"})
    game = game_title.text

    '''SPORT'''
    div_breadcrumb = soup2.find("div", {"class": "breadcrumb"})
    ul_breadcrumb = div_breadcrumb.find("ul")
    lis_breadcrumb = ul_breadcrumb.findAll("li")
    sport = lis_breadcrumb[1].text
    league = lis_breadcrumb[2].text

    '''MARKETS'''
    next_markets = soup2.find("div", {"class": "prox_eventos"})
    markets = next_markets.findAll(
        "ul", {"market-group-id": "market.MarketGroupId"})
    game_info = [{'date': date}, {'game': game},
                 {'sport': sport}, {'league': league}]
    markets_array = []
    for market in markets:
        market_des = market["des"]
        odds_toggle = market.find("li", {"class": "ksToggle"})
        market_odds_div = odds_toggle.find(
            "div", {"class": "apuestas_partido"})
        market_odds_a = market_odds_div.findAll("a")

        odds_array = []
        for odd_a in market_odds_a:
            des = odd_a["des"]
            coef = odd_a.find("span", {"class": "coef"})
            odd = coef.text

            odds_array.insert(len(odds_array), [{'des': des}, {'odd': odd}])
        markets_array.insert(len(markets_array), [
                             {'des': market_des}, {'odds': [odds_array]}])

    game_data = {'info': game_info, 'markets': markets_array}
    print(game_data)
    url = 'http://localhost:3000/api/odds'
    x = requests.post(url, data=game_data)
    time.sleep(0.1)


def extractLeagues():
    with open('ligas.html', 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'html')
        general_ul = soup.find("ul", {"class": "ksAccordion-toggle"})
        li_array = general_ul.findAll("li")

        for row in li_array:

            div_section = row.find("div", {"class": "seccion"})
            a_section = div_section.find("a")
            link = 'https://euskadi.kirolbet.es'+a_section['href']
            extractMatchList(link)


''' extractLeagues() '''
extractMarkets("https://euskadi.kirolbet.es/esp/Sport/Evento/2148667")
