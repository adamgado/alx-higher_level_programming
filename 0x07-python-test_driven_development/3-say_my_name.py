#!/usr/bin/python3
"""Module for say_my_name function"""


def say_my_name(first_name, last_name=""):
    """print first and last name

    Args:
        first_name: first name string
        last_name: last name string

    Raises:
        TypeError: first_name or last_name not string
    """
    if type(first_name) not in (str):
        raise TypeError("first_name must be a string")

    if type(last_name) not in (str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
