#!/usr/bin/python3
"""email as a parameter, and displays the body of the response"""
from urllib.request import Request, urlopen
from sys import argv
from urllib.parse import urlencode


if __name__ == "__main__":
    email = urlencode({'email': argv[2]}).encode('ascii')
    lnk = Request(argv[1], email)

    with urlopen(lnk) as r:
        print(r.read().decode('utf-8'))
