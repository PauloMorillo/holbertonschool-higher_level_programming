#!/usr/bin/python3
"""This module fetches a url"""

if __name__ == "__main__":
    import requests
    req = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req))
