#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as response:
        content = response.read()
        print("content response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
