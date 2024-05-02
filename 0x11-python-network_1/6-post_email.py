#!/usr/bin/python3
"""sends a POST request to the passed URL"""
import requests
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    lnk = requests.post(argv[1], email)

    print(lnk.text)
