# coding: utf-8
"""
tweetsandprices
Created on 2/6/2018 12:41 PM
@author: Ian
""" 

import pandas as pd
import numpy as np

def extract_text(tweets):
    df = pd.read_json(tweets)
    df['date'] = df['timestamp'].apply(lambda x: x.date())
    df = df.drop(['fullname','id','likes','replies','retweets','url','user', 'timestamp'], axis=1)
    
    return df