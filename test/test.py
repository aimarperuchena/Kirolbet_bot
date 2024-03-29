from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless") 

driver = webdriver.Chrome(executable_path='chromedriver',   chrome_options=chrome_options)  


driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window() 
driver.get("https://euskadi.kirolbet.es/esp/Sport/Evento/2222407")
elem = driver.find_element_by_xpath("//*")
html = elem.get_attribute("outerHTML")



    
try:

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
  print(span_date)
  date_time = span_date['title']
  date_time = date_time.split(" ")
  date = date_time[0]
  times = date_time[1]
  times = times.replace("Z", "")
  '''GAME TEAMS'''
  game_title = soup2.find("h3", {"class": "titulo_seccion"})
  game = game_title.text
  print(game)
except Exception as e:
        print(e)
time.sleep(100000)
driver.close()