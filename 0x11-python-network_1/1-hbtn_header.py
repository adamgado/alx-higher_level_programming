#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    lnk = Request(argv[1])

    with urlopen(lnk) as r:
        print(dict(r.headers).get("X-Request-Id"))
