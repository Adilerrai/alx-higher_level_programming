#!/usr/bin/python3
"""Creating something"""

import requests

if __name__ == "__main__":
    url = requests.get("https://alx-intranet.hbtn.io/status")
    data = url.text
    resType = type(data)
    print(f"Body response:\n\t- type: {resType}\n\t- content: {data}")
