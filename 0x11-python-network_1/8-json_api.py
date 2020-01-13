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
    values = {'q': value}
    req = requests.post("http://0.0.0.0:5000/search_user", data=values)
    js = req.json()
    if js:
        try:
            print("[{}] {}".format(js['id'], js['name']))
        except:
            print("Not a valid JSON")
    else:
        print("No result")
