#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class function"""
    def area(self):
        """raise exception message"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """value validating function"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
