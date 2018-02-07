# coding: utf-8
"""
tweetsandprices
Created on 2/6/2018 2:15 PM
@author: Ian
""" 

from bs4 import BeautifulSoup
from urllib import request
from datetime import datetime

# the goal of this docstring is to return article text information along with its date
# the text information will be further analyzed later on
def scrape_article(url):
    opener = request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    soup = BeautifulSoup(opener.open(url), 'html.parser')
    
    # parse the date information on each article to only return a date
    strtime = soup.time.attrs['datetime']
    strtime = strtime[:10]
    date = datetime.strptime(strtime, "%Y-%m-%d").date()
    print(date)
    
    text = ''
    for p in soup.find_all('p'):
        text += p.get_text()
    
    text = text[8:text.find("What do you think")]   # I cut out the first 9 characters because it is always not part of the text
    # the What do you think part is somewhat of an assumption that all the articles on Bitcoin news will end with that question
    # This assumption does not hold true for older articles but checking an article on Dec 1, 2017 shows that it still exists so
    # that is where I am cutting off 
    
    
    
    print(text)
    
