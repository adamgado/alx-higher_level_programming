#!/usr/bin/python3
"""defines a 'Square' class"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes a new Square.

        Args:
            size : size of the new square.

        raises errors
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """set position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns area of the new square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with the #s."""
        if self.__size == 0:
            print("")
            return

        [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for c in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")
