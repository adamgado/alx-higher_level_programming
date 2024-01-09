#!/usr/bin/python3
"""add_attribute function"""


def add_attribute(objct, new_attribute, value):
    """add attribute to object"""
    if ('__dict__' in dir(objct)):
        setattr(objct, new_attribute, value)
    else:
        raise TypeError("can't add new attribute")
