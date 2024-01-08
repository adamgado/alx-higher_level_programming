#!/usr/bin/python3
"""Mylist class function"""


class MyList(list):
    """define class mylist that inherits list"""
    def print_sorted(self):
        """print list of ints sorted"""
        print(sorted(self))

if __name__ == "__main__":
     import doctest
     doctest.testfile("tests/1-my_list.txt")
