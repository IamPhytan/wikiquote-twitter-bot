#! /usr/bin/env python3
# coding: utf-8

import json
import sys

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

    

