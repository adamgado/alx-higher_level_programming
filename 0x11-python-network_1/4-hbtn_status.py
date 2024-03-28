#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    lnk = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {}'.format(type(lnk.text)))
    print('\t- content: {}'.format(lnk.text))
