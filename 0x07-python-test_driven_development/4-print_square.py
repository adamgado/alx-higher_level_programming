#!/usr/bin/python3
"""Module for print_square function"""


def print_square(size):
    """print a square with #s

    Args:
        size: int size of square's side

    Raises:
        TypeError: size is not int
        ValueError: size is negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
