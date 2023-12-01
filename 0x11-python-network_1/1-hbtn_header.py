#!/usr/bin/python3
"""Creating something """
import sys
from urllib.request import urlopen
with urlopen(sys.argv[1]) as response:
        body = response

header = body.__dict__['headers']
for key, val in header.items():
    if key == 'X-Request-Id':
        print(val)
