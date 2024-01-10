#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """append string to end of utf8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
