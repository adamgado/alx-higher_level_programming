#!/usr/bin/python3
"""pascal_triangle function"""


def pascal_triangle(n):
    """return list of lists of integers represent the triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        last_row = triangle[-1]
        temp = [1]
        for i in range(len(last_row) - 1):
            temp.append(last_row[i] + last_row[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
