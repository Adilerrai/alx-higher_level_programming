#!/usr/bin/python3
"""Creating something """
import sys
from urllib.request import urlopen
with urlopen(sys.argv[1]) as response:
    x_request_id = response.headers.get('X-Request-Id')

print(x_request_id)
