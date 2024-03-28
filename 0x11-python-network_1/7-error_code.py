#!/usr/bin/python3
"""HTTP status code is greater than or equal to 400 print Error code"""
import requests
from sys import argv


if __name__ == "__main__":
    lnk = requests.get(argv[1])

    if lnk.status_code >= 400:
        print('Error code:', lnk.status_code)
    else:
        print(lnk.text)
