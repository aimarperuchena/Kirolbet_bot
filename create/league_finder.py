import urllib.request
import pymysql
import urlopen
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime
from datetime import date
import pymysql.cursors
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import re

def read_html(html):
    print('read html')
    soup2 = BeautifulSoup(html, "html.parser")
    links=soup2.find_all('a', attrs={'href': re.compile("^/esp/Sport/Competicion")})
    for link in links:
        with open('somefile.txt', 'a') as the_file:
            the_file.write(link.text+'\n')
    print(len(links))
def open_window():
    driver=webdriver.Chrome("chromedriver.exe")
    driver.get('https://euskadi.kirolbet.es')

    consent_button=driver.find_element_by_class_name("consent-give")
    consent_button.click()
    lis=driver.find_elements_by_class_name("dcjq-parent-li")
    for li in lis:
        li.click()
        links=li.find_elements_by_xpath("//a[contains(@href, '/esp/Sport/Competicion')]")
        for link in links:
            try:
                if link.text!='':
                    with open('somefile.txt', 'a') as the_file:
                        the_file.write(link.text+'\n')
            except a as identifier:
                pass
        with open('somefile.txt', 'a') as the_file:
            the_file.write('---------------------\n')
    print(len(lis))

    time.sleep(1000)
def main():
    open_window()
main()