#!/usr/bin/python3
"""This module fetches a url"""

if __name__ == "__main__":
    import sys
    import urllib.request
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
