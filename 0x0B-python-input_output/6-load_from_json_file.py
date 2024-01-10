#!/usr/bin/python3
"""load_from_json_file function"""
import json


def load_from_json_file(filename):
    """return python object from a json file"""
    with open(filename) as f:
        return json.load(f)
