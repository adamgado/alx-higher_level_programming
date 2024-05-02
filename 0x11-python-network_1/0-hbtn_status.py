#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    lnk = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(lnk) as r:
        content = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
