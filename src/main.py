# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:49:41 2018

@author: ho
"""

import datetime
import tweet_tle
import article_scrape
import btc_scrape
import pandas as pd
import matplotlib.pyplot as plt
import timeit

bitcoin_tweets_path = '../include/bitcoin_tweets.json'
crawl_url = 'https://news.bitcoin.com/page/' 
btc_url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
start_date = datetime.date(2018, 2, 6)  # go backwards because the iterator has most recent articles first
end_date = datetime.date(2018, 1, 31)   # one week

def create_articleDF():
    # extracting all the text from news.bitcoin.com from january 31 to february 6
    links = set()
    page_num = 1
    while (article_scrape.find_date(crawl_url + str(page_num)) >= end_date):
        templist = article_scrape.crawl_articles(crawl_url + str(page_num))
        for l in templist:
            links.add(l)
        page_num += 1
    
    article_df = pd.DataFrame()
    links = list(links)
    for link in links:
        temp_df = article_scrape.scrape_article(link)
        article_df = pd.concat([article_df, temp_df], axis=0)
    
    article_df = article_df[article_df['date'] <= start_date]
    article_df = article_df.sort_values(by=['date'])
    article_df = article_df.reset_index(drop=True)
    
    return article_df

def create_tweetDF():
    # extracting all the tweets from twitter about bitcoin from january 31 to february 6
    return tweet_tle.extract_text(bitcoin_tweets_path)

def create_btcDF():
    # extracting all the prices of btc from january 31 to february 6
    return btc_scrape.price_scrape(btc_url, end_date, start_date)

def main():
    adf = create_articleDF()    # takes roughly over a minute on laptop
    tdf = create_tweetDF()
    # the text is to be analyzed for sentiment (positive or negative[most likely something simple])
    
    bdf = create_btcDF()
    # later we correlate the sentiment analyzed text and the prices for the next day
    
    
    
if __name__ == '__main__':
    main()