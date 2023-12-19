#!/usr/bin/python3
"""defines a 'Square' class"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """initializes a new Square.

        Args:
            size : size of the new square.
        raises errors
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
