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

with open('pokerstars_ligas.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'html')

    general_section=soup.find("section")
    competitions=general_section.findAll("div",{"class":"competitionListItem"})
    for competition in competitions:
        link_tag=competition.find("a")
        print(link_tag.text)