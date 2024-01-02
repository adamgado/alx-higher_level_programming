#!/usr/bin/python3
"""module for the addition method"""


def add_integer(a, b=98):
    """adds two numbers

    Args:
        a: first number
        b: second number, default 98

    Raises:
        TypeError: if a, b are not int or float

    Returns:
        sum of the two numbers
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
