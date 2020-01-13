#!/usr/bin/python3
"""This module get id for a github user with basic authentication"""

if __name__ == "__main__":
    import sys
    import requests
    try:
        user = sys.argv[1]
        passw = sys.argv[2]
    except:
        user = ""
        passw = ""
    req = requests.get("https://api.github.com/user", auth=(user, passw))
    try:
        js = req.json()
    except:
        js = dict()
    if js:
        try:
            print(js['id'])
        except:
            print("None")
    else:
        print("None")
