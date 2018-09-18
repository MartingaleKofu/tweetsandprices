# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:49:41 2018

@author: ho
"""

import datetime
import article_scrape
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import nltk

bitcoin_tweets_path = '../include/bitcoin_tweets.json'
crawl_url = 'https://news.bitcoin.com/page/' 
btc_url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
start_date = datetime.date(2018, 2, 6)  # go backwards because the iterator has most recent articles first
end_date = datetime.date(2018, 1, 31)   # one week

def find_start_date(url, start, beg, end):
    mid = int((beg + end)/2)
    date = article_scrape.find_date(url + str(mid))
    if (date == start):
        return mid
    elif (date > start):
        return find_start_date(url, start, mid, end)
    else:
        return find_start_date(url, start, beg, mid)
    
def request_sentiment(text):
    url = 'http://text-processing.com/api/sentiment/'
    text = 'text='+text
    r = requests.post(url, data=text)
    return r.json()

def main():
    # extracting all the text from news.bitcoin.com from january 31 to february 6
    
    """
    d = {'col1':[1,2], 'col2':['great','goodbye']}
    random_df = pd.DataFrame(data=d)
    random_df['sentiment_score'] = random_df['col2'].apply(request_sentiment)
    print(random_df)
    return 0
    """
    
    links = set()
    # use divide and conquer to find the start date quicker because the list will always keep growing
    page_num = article_scrape.num_pages(crawl_url + str(1))
    start_page = find_start_date(crawl_url ,start_date, 1,page_num)
    content_date = article_scrape.find_date(crawl_url + str(start_page))
    while (content_date >= end_date):
        if (content_date - start_date).days > 0:
            start_page += 1
            content_date = article_scrape.find_date(crawl_url + str(start_page))
            continue
        templist = article_scrape.crawl_articles(crawl_url + str(start_page))
        for l in templist:
            links.add(l)
        start_page += 1
        content_date = article_scrape.find_date(crawl_url + str(start_page))
    
    article_df = pd.DataFrame()
    links = list(links)
    for link in links:
        temp_df = article_scrape.scrape_article(link)
        article_df = pd.concat([article_df, temp_df], axis=0)
    
    article_df = article_df[article_df['date'] <= start_date]
    article_df = article_df.sort_values(by=['date'])
    article_df = article_df.reset_index(drop=True)
    # all articles in a dataframe sorted by date
    # we can now perform sentiment analysis on each article to give it a score before we try to find correlation between sentiment and prices
    
    # strategy: we can perform sentiment analysis on each sentence of each article and average/sum up the sentiment scores before deciding the overall sentiment score
    # of eah article
    article_df['sentences'] = article_df['text'].apply(nltk.sent_tokenize)
    print(article_df['sentences'])
    return 0
    article_df['json_information'] = article_df['text'].apply(request_sentiment) # first split the article into sentences using nltk.data
    
    print(article_df)
    
    return article_df
    
    
if __name__ == '__main__':
    main()