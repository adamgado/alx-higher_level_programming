#!/usr/bin/python3
"""save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """write object to a text file as json string"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
