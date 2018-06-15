import wikiquote

def get_quotes_from_author(author):

    quotes = wikiquote.quotes(author)

    tweets = ["{0} - {1}".format(quote, author) for quote in quotes]

    return tweets




