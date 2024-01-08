#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """return if object inherits a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
