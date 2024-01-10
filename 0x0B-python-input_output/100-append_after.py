#!/usr/bin/python3
"""append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """add text after a string in a file"""
    new_text = ""
    with open(filename) as r:
        for line_string in r:
            new_text += line_string
            if search_string in line_string:
                new_text += new_string
    with open(filename, "w") as w:
        w.write(new_text)
