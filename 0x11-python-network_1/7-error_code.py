#!/usr/bin/python3
"""Documentated """
from requests import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.get(url)
    if req.stats_code >= 400:
        print(f"Error code: {req.status_code}")
        ecit()
    else:
        print("index")
