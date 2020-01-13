#!/usr/bin/python3
"""This module fetches a url"""

import sys
import urllib.parse
import urllib.request
url = sys.argv[1]
value = sys.argv[2]
values = {'email': value}
data = urllib.parse.urlencode(values)
data = data.encode("utf-8")
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode("utf-8"))
