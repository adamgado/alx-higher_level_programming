#!/usr/bin/python3
"""define Locked class"""


class LockedClass:
    """prevent initialization of attribute except 'first_name' """
    __slots__ = 'first_name'
