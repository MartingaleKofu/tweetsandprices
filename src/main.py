# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:49:41 2018

@author: ho
"""

import datetime
import tweet_tle
import article_scrape
import pandas as pd
import numpy as np

bitcoin_tweets_path = '../include/bitcoin_tweets.json'
crawl_url = 'https://news.bitcoin.com/page/' 
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

def main():
    # extracting all the text from news.bitcoin.com from january 31 to february 6
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
    
    print(links)
    article_df = pd.DataFrame()
    links = list(links)
    for link in links:
        temp_df = article_scrape.scrape_article(link)
        article_df = pd.concat([article_df, temp_df], axis=0)
    print(article_df)
    
    article_df = article_df[article_df['date'] <= start_date]
    article_df = article_df.sort_values(by=['date'])
    article_df = article_df.reset_index(drop=True)
    
    # extracting all the tweets from twitter about bitcoin from january 31 to february 6
    tweet_tle.extract_text(bitcoin_tweets_path)
    
if __name__ == '__main__':
    main()