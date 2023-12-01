#!/usr/bin/python3
"""Creating something"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    r = requests.post(url, data=data)
    if r.text >= 400:
        print(f"Error code: {r.text}")
    else:
        print(r.text)
