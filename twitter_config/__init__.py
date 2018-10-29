import tweepy
import random

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


def choose_quote_n_tweet(quotes, used_tweets_idxs, api):
    quote_idx = random.randint(0, len(quotes) - 1)

    if quote_idx in used_tweets_idxs:
        used_tweets_idxs = choose_quote_n_tweet(quotes, used_tweets_idxs, api)
    else:
        api.update(status=quotes[quote_idx])
        used_tweets_idxs.append(quote_idx)

    return used_tweets_idxs
