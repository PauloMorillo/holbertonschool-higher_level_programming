#!/usr/bin/python3
"""This module fetches a url with POST method and shows the response"""

if __name__ == "__main__":
    import sys
    import requests
    values = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=values)
    print(req.text)
