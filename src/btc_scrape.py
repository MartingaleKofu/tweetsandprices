# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:04:58 2018

@author: Ian
"""

import json
import datetime
import pandas as pd
from urllib import request

def price_scrape(url, start, end):
    start = start.strftime('%Y-%m-%d')
    end = end.strftime('%Y-%m-%d')
    
    url = url + '?start=' + start + '&end=' + end
    opener = request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    
    btc = opener.open(url)
    btc_json = json.load(btc)
    btc_pd = pd.DataFrame(btc_json)
    btc_pd = btc_pd.drop(['disclaimer', 'time'], axis=1)
    btc_pd = btc_pd.drop(['updated', 'updatedISO'])
    btc_pd = btc_pd.reset_index()
    btc_pd.columns = ['date', 'price']
    btc_pd['date'] = btc_pd['date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").date())
    
    return btc_pd