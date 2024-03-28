#!/usr/bin/python3
"""takes your GitHub credentials and uses the GitHub API to display your id"""
import requests
from sys import argv


if __name__ == "__main__":
    repo = '{}/repos/{}/{}/commits'.format('https://api.github.com',
                                           argv[2], argv[1])
    lnk = requests.get(repo).json()

    for commits in lnk[0:10]:
        print(commits['sha'] + ':', commits['commit']['author']['name'])
