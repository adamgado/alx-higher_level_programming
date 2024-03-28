#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header"""
import requests
from sys import argv


if __name__ == "__main__":
    lnk = requests.get(argv[1])

    print(lnk.headers.get('X-Request-Id'))
