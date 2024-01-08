#!/usr/bin/python3
"""Mylist class function"""


class MyList(list):
    """define class mylist that inherits from list"""
    def print_sorted(self):
        """print list of ints sorted"""
        print(sorted(self))
