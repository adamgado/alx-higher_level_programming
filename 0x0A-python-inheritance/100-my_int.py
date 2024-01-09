#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """methods: __init__, __eq__, __ne___"""
    def __init__(self, number):
        """initialize number"""
        self.number = number

    def __eq__(self, other_number):
        """return: true if not equal"""
        return self.number != other_number

    def __ne__(self, other_number):
        """return: true if equal"""
        return self.number == other_number
