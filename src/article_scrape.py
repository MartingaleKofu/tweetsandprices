# coding: utf-8
"""
tweetsandprices
Created on 2/6/2018 2:15 PM
@author: Ian
""" 

import re
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from urllib import request

# the goal of this docstring is to return article text information along with its date
# the text information will be further analyzed later on
def scrape_article(url):
    opener = request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    soup = BeautifulSoup(opener.open(url), 'html.parser')
    
    # parse the date information on each article to only return the published date
    time = soup.find('meta', property='article:published_time')
    strtime = time['content']
    strtime = strtime[:10]
    date = datetime.datetime.strptime(strtime, "%Y-%m-%d").date()
    
    text = ''
    for p in soup.find_all('p'):
        text += p.get_text()
    
    text = text[8:text.find("What do you think")]   # I cut out the first 9 characters because it is always not part of the text
    # the What do you think part is somewhat of an assumption that all the articles on Bitcoin news will end with that question
    # This assumption does not hold true for older articles but checking an article on Dec 1, 2017 shows that it still exists so
    # that is where I am cutting off 
    d = {'date': [date], 'text': [text]}
    
    df = pd.DataFrame(data=d)
    return df
    
def crawl_articles(url):
    opener = request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    soup = BeautifulSoup(opener.open(url), 'html.parser')
    
    links = []  # list of url's in string
    for link in soup.find_all('a', href=True, rel='bookmark'):
        if (link['title'] == link.get_text()):
            links.append(link['href'])
    return links

def find_date(url):
    opener = request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    soup = BeautifulSoup(opener.open(url), 'html.parser')
    strtime = soup.time.attrs['datetime']
    strtime = strtime[:10]
    date = datetime.datetime.strptime(strtime, "%Y-%m-%d").date()

    return date

def num_pages(url):
    opener = request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    soup = BeautifulSoup(opener.open(url), 'html.parser')
    words = soup.find_all('span', attrs={"class":"pages"})[0].get_text().split(' ')
    numpages = int(words[-1])
    
    return numpages
