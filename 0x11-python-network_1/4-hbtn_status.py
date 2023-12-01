#!/usr/bin/python3

import requests 
if __name__ == "__main__":
    url = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("    - type:", type(url.text))
    print("    - content:", url.text)
