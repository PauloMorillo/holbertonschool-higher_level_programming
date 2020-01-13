#!/usr/bin/python3
"""This module fetches a url with POST method and shows the response"""

if __name__ == "__main__":
    import sys
    import requests
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
