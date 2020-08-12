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


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = 'https://deportes.marcaapuestas.es/es/t/48352/Segunda'
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()
soup2 = BeautifulSoup(html)


table=soup2.find("table",{"class":"coupon"})
trs=table.findAll("tr")
for tr in trs:
    time=''
    date=''
    
    '''TIME DATE'''
    time_td=tr.find("td",{"class":"time"})
    timeSpan=time_td.find("span",{"class":"time"})
    dateSpan=time_td.find("span",{"class":"date"})
    date=dateSpan.text
    time=timeSpan.text










''' with open('marca_ligas.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'html')

    ul_classes = soup.find("ul")
    expanders = ul_classes.findAll("li", {"class": "expander"})
    for expander in expanders:
        ul_expanders = expander.findAll("ul", {"class": "expander-content"})
        for ul_expander in ul_expanders:
            lis = ul_expander.findAll("li")
            for li in lis:
                a = li.find("a")
                name = a.text
                link = a['href'] '''
