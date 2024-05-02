#!/usr/bin/python3
"""function that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    db = list_of_integers
    if db == []:
        return None
    db_len = len(db)
    first, last = 0, db_len - 1
    while first < last:
        middle = first + (last - first) // 2
        if db[middle] > db[middle - 1] and db[middle] > db[middle + 1]:
            return db[middle]
        if db[middle - 1] > db[middle + 1]:
            last = middle
        else:
            first = middle + 1
    return db[first]
