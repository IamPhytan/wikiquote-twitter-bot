import tweepy


def create_twitter_config(config):

    consumer_key = config['TWITTER']["CONSUMER_KEY"]
    consumer_secret = config['TWITTER']["CONSUMER_SECRET"]
    access_token = config['TWITTER']["ACCESS_TOKEN"]
    access_token_secret = config['TWITTER']["ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api

