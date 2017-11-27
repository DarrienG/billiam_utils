#!/usr/bin/env python3

import requests
import sys

POST_TWEET_LINK = "http://api.darrienglasser.com:8090/posttweet"

SECRET_KEY = ""
tweet_data = {"secretKey":SECRET_KEY, "tweetText":sys.argv[1]}
r = requests.post(POST_TWEET_LINK, data=tweet_data)

print("TWEET POSTED 🙏")
print(r.text)
print(r.status_code)
