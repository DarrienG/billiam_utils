#!/usr/bin/env python3

import requests
import sys
import os

POST_TWEET_LINK = ""
SECRET_KEY = ""

if len(sys.argv) < 2:
    raise Exception("Need -b for Bill or -j for Jay and tweet text in a string afterwards")

arg = sys.argv[1].lower()

if sys.argv[1] == "-b":
    POST_TWEET_LINK = "http://api.darrienglasser.com:8090/postbill"
    SECRET_KEY = "INSERT_BILL_KEY"
elif sys.argv[1] == "-j":
    POST_TWEET_LINK = "http://api.darrienglasser.com:8090/postjay"
    SECRET_KEY = "INSERT_JAY_KEY"
elif sys.argv[1] == "-h":
    print("Command usage\n\t-b \"<TWEET>\" to post to Bill\n\t-j \"<TWEET>\" to post to Jay\n\t-h for help")
    os.exit(1)
else:
    raise Exception("Invalid account to tweet to. Use -b for Bill or -j for Jay")

tweet_data = {"secretKey":SECRET_KEY, "tweetText":sys.argv[2]}
r = requests.post(POST_TWEET_LINK, data=tweet_data)

if r.status_code != 202:
    print("Failed to post tweet 😢")
    print("Error code:" + str(r.status_code))
else:
    print("TWEET POSTED 🙏")
    print(r.text)
    print(r.status_code)
