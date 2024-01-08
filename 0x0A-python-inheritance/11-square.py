#!/usr/bin/python3
"""square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inherits rectangle"""
    def __init__(self, size):
        """initialize size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """square area"""
        return self.__size ** 2

    def __str__(self):
        """string representation of square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
