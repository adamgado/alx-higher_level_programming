#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions"""
from urllib.request import Request, urlopen
from sys import argv
from urllib.error import HTTPError


if __name__ == "__main__":
    lnk = Request(argv[1])

    try:
        with urlopen(lnk) as r:
            print(r.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
