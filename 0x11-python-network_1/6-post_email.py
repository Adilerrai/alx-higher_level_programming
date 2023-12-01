#!/usr/bin/python3
"""Creating something"""

import sys
import requests
import json

url = sys.argv[1]

data = {"email": sys.argv[2]}

r = requests.post(url, json=data)

print(r.text)
