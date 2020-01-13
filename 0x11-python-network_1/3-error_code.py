#!/usr/bin/python3
"""This module fetches a url"""

if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
