#!/usr/bin/python3
"""Doc"""

import sys
import requests
if __name__ == "__main__":
    url = requests.get(sys.argv[1])
    data = url.headers.get("X-Request-Id")

    print(data)
