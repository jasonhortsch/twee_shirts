# code taken and then slightly modified from here: 
# http://www.danielforsyth.me/analyzing-a-nhl-playoff-game-with-twitter/

from config import *
import tweepy
import sys
import pymongo

# consumer keys and access tokens are kept in a separate file for security
# they are read in from the config.py file above
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        # initializing the database that the tweets will be added to
        self.db = pymongo.MongoClient().NBA

    def on_status(self, status):
        # remove the commas to make working with csv files easier and smoother
        no_commas = status.text.replace(",", "")

        data ={}
        data['text'] = no_commas
        data['created_at'] = status.created_at
        data['geo'] = status.geo
        data['source'] = status.source

        # checking that a given tweet actually contains hashtags
        # only if it contains hashtags is it added to the database
        # this helps with storage and efficiency
        if "#" in no_commas:
            # print the tweet so tweets can be seeing scrolling by
            # this is both fun, and lets you know the script is working
            print no_commas
            # insert the tweet into the database collection
            self.db.Tweets.insert(data)

    # a check that the original author, daniel forsythe put in
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    # another check that the original author put in
    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))

# the actual term that is being searched for in the tweets
sapi.filter(track=['nba'])
