# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:49:41 2018

@author: ho
"""

import tweet_tle
import yahooscrape

bitcoin_tweets_path = '../include/bitcoin_tweets.json'

def main():
    tweet_tle.extract_text(bitcoin_tweets_path)
    
if __name__ == '__main__':
    main()