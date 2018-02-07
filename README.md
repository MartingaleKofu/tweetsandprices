README

In this mini project, I will be trying to find some correlation between
Tweets and Bloomberg Articles about Bitcoin/BTC and the resulting prices
the next day.

To scrape twitter data I used twitterscraper (https://github.com/taspinar/twitterscraper)
and to scrape Bitcoin News I used BeautifulSoup4 and then parsed the data with 
Natural Language Toolkit (NLTK)

After installing twitterscraper, I use this command to scrape roughly 6000
tweets between December 8th, 2017 and February 6th, 2018:
twitterscraper -bd 2018-01-31 -ed 2018-02-06 "Bitcoin OR BTC" -o bitcoin_tweets.json -l 20000
