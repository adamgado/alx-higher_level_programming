#!/usr/bin/python3
"""takes your GitHub credentials and uses the GitHub API to display your id"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    a = HTTPBasicAuth(argv[1], argv[2])
    lnk = requests.get("https://api.github.com/user", auth=a)

    print(lnk.json().get('id'))
