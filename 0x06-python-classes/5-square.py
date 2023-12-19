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
        self.size = size

    @property
    def size(self):
        """set size of the square."""
        return (self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns area of the new square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with the #s."""
        for a in range(self.__size):
            for b in range(self.__size):
                print("#", end="")
            print("\n")
