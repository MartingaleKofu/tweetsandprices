# coding: utf-8
"""
tweetsandprices
Created on 2/6/2018 2:15 PM
@author: Ian
""" 

from bs4 import BeautifulSoup
from urllib import request

def scrape_article(url):
    opener = request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    soup = BeautifulSoup(opener.open(url))

    print(soup.prettify())

url = "https://news.bitcoin.com/australia-to-ban-bitcoin-gambling/"

scrape_article(url)