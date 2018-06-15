import wikiquote
import os

# Name: Wikiquote Twitter Bot
# Desc: A simple way to tweet famous quotes from Wikiquote
# Repo: https://github.com/IamPhytan/wikiquote-twitter-bot
# Author: IamPhytan
# License: MIT
# Path: -/wikiquote_import

def get_quotes_from_author(quotes, author):

    author_quotes = wikiquote.quotes(author)
    tweets = ["{0} - {1}".format(quote, author) for quote in author_quotes]

    for tweet in tweets:
        quotes.append(tweet)

    return quotes


def get_quotes(config):

    quotes = list()
    authors = config['WIKIQUOTE']['FAMOUS_PEOPLE']

    for author in authors:
        quotes = get_quotes_from_author(quotes, author)

    save_quotes_to_file(quotes)

    return quotes


def save_quotes_to_file(quotes):
    filename = 'saved_quotes.txt'

    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'

    with open(filename, append_write) as f:
        for quote in quotes:
            f.write("%s\n" % quote)

