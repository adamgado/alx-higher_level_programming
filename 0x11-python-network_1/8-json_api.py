#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user with the letter"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''
    lnk = requests.post("http://0.0.0.0:5000/search_user", {"q": q})

    try:
        content = lnk.json()
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get("id"), content.get("name")))
    except ValueError:
        print("Not a valid JSON")
