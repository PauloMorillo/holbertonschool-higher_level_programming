#!/usr/bin/python3
"""This module fetches a url"""

if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print("Body response:")
    print("    - type:", type(html))
    print("    - content:", html)
    print("    - utf8 content:", html.decode("utf-8"))
