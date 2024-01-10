#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """print content of utf8 text file to standard output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
