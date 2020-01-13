#!/usr/bin/python3
"""This module fetches a url with POST method and shows the response
and decode JSON

"""

if __name__ == "__main__":
    import sys
    import requests
    try:
        value = sys.argv[1]
    except:
        value = ""
    req = requests.get("https://swapi.co/api/people/?search=" + value)
    try:
        js = req.json()
    except:
        js = dict()
    if js:
        print("Number of results: {}".format(js['count']))
        # print(type(js))
        # print(js)
        a = 0
        while a < len(js['results']):
            peop = js['results'][a]
            # print(type(peop))
            print(peop['name'])
            a = a + 1
    else:
        print("Number of results: 0")
