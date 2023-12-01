#!/usr/bin/python3
"""Script see the body response """

from urllib.request import urlopen
if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
    print("Body response:")
    print(f"    - type: {body.__class__}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")
