# Wikiquote Twitter Bot
> A simple way to tweet famous quotes from Wikiquote

![GitHub release](https://img.shields.io/github/tag/iamphytan/wikiquote-twitter-bot.svg?label=version&style=flat-square)
![GitHub Issues](https://img.shields.io/github/issues/iamphytan/wikiquote-twitter-bot.svg?style=flat-square)
![Downloads](https://img.shields.io/github/downloads/iamphytan/wikiquote-twitter-bot/total.svg?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)

## Motivation
I wanted to have a bot that would tweet different quotes from Wikiquote each morning to start the day on a good note. 
This small scripts uses Tweepy's [API](https://github.com/tweepy/tweepy) and fredericotdn's 
[Wikiquote API](https://github.com/federicotdn/python-wikiquotes) to scan quotes on Wikiquote and tweet them .

## Installation
The following steps explain how to configure the script before running it:
 1. Clone the repo: `git clone https://github.com/IamPhytan/wikiquote-twitter-bot.git`
 2. Download the requirements (or create a `virtualenv` before) : `pip3 install -r requirements.txt`
 3. Follow [this tutorial](https://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/) to get your :
    * Consumer key
    * Consumer secret
    * Access token
    * Access token secret
 4. Add these values to the [configuration file]
 5. Insert in the same [configuration file] the time you want to send quotes and the names of the people who inspire you.
 6. Run the script: `python3 main.py`

## License
[MIT](https://opensource.org/licenses/MIT)

[configuration file]: config.json