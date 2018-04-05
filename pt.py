#!/usr/bin/env python3

import requests
import sys

cmd_usage = "Command usage\n\t-b \"<TWEET>\" to post to Bill\n\t-j \"<TWEET>\" to post to Jay\n\t-h for help" 

POST_TWEET_LINK = ""
SECRET_KEY = ""

if len(sys.argv) < 2:
    print("Not enough arguments")
    print(cmd_usage)
    sys.exit(1)

arg = sys.argv[1].lower()

if sys.argv[1] == "-b":
    POST_TWEET_LINK = "http://api.darrienglasser.com:8090/postbill"
    SECRET_KEY = "INSERT_BILL_KEY"
elif sys.argv[1] == "-j":
    POST_TWEET_LINK = "http://api.darrienglasser.com:8090/postjay"
    SECRET_KEY = "INSERT_JAY_KEY"
elif sys.argv[1] == "-h":
    print(cmd_usage)
    sys.exit(1)
else:
    print("Invalid flag")
    print(cmd_usage)
    exit(1)

tweet_data = {"secretKey":SECRET_KEY, "tweetText":sys.argv[2]}
r = requests.post(POST_TWEET_LINK, data=tweet_data)

if r.status_code != 202:
    print("Failed to post tweet 😢")
    print("Error code:" + str(r.status_code))
    print("Response: " + r.text)
else:
    print("TWEET POSTED 🙏")
    print(r.text)
    print(r.status_code)
