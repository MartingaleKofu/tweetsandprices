# coding: utf-8
"""
tweetsandprices
Created on 2/6/2018 12:41 PM
@author: Ian
""" 

import pandas as pd

def is_ascii(string):
    return all(ord(char) < 128 for char in string)

def extract_text(tweets):
    df = pd.read_json(tweets)
    df['date'] = df['timestamp'].apply(lambda x: x.date())
    df = df.drop(['fullname','id','likes','replies','retweets','url','user', 'timestamp'], axis=1)
    
    # remove all rows with non ascii characters, cause I don't know how to analyze that
    df = df[df['text'].apply(is_ascii)]
    df = df.sort_values(by=['date'])
    df = df.reset_index(drop=True)
    
    return df