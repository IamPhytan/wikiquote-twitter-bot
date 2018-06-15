import tweepy

# Name: Wikiquote Twitter Bot
# Desc: A simple way to tweet famous quotes from Wikiquote
# Repo: https://github.com/IamPhytan/wikiquote-twitter-bot
# Author: IamPhytan
# License: MIT
# Path: -/twitter_config

def create_twitter_config(config):

    consumer_key = config['TWITTER']["CONSUMER_KEY"]
    consumer_secret = config['TWITTER']["CONSUMER_SECRET"]
    access_token = config['TWITTER']["ACCESS_TOKEN"]
    access_token_secret = config['TWITTER']["ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api

