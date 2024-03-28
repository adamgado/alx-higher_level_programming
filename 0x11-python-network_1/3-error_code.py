#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
from urllib.request import Request, urlopen
from sys import argv
from urllib.parse import urlencode


if __name__ == "__main__":
    lnk = Request(argv[1])

    try:
        with urlopen(lnk) as r:
            print(r.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code:', err.code)
