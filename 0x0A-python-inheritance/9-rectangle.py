#!/usr/bin/python3
"""rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialize width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation function"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
