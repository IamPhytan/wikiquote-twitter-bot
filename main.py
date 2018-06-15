#! /usr/bin/env python3
# coding: utf-8

import json
import sys
import wikiquote_import as wq_imp
import twitter_config as tw_conf
import datetime as dt

# Name: Wikiquote Twitter Bot
# Desc: A simple way to tweet famous quotes from Wikiquote
# Repo: https://github.com/IamPhytan/wikiquote-twitter-bot
# Author: IamPhytan
# License: MIT
# Path: -


if __name__ == '__main__':

    assert (sys.version_info[0] >= 3), "Python 3 or a more recent version is required."

    with open('config.json', 'r') as f:
        config = json.load(f)

    quotes = wq_imp.get_quotes(config)

    quotes_to_send = [pot_tweet for pot_tweet in quotes if len(pot_tweet) <= 280]

    tw_api = tw_conf.create_twitter_config(config)

    used_tweets_idxs = list()

    while len(used_tweets_idxs) < len(quotes_to_send):
        curr_tm = dt.datetime.now().time()

        if (curr_tm.hour, curr_tm.minute, curr_tm.second, curr_tm.microsecond) == (8, 0, 0, 0):
            used_tweets_idxs = tw_conf.choose_quote_n_tweet(quotes_to_send, used_tweets_idxs, tw_api)

    print("Add more quotes")



