#!/usr/bin/python3
"""Module for matrix_divided function"""


def matrix_divided(matrix, div):
    """divide elements of matrix by div
    Args:
        matrix: List of lists containing int or float
        div: number to divide matrix by
    Returns:
        list: new matrix
    Raises:
        TypeError: div is not int or float
        TypeError: matrix is not list of lists containing int or float
        TypeError: sublists are not all same size
        ZeroDivisionError: div is zero
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    iif type(matrix) not in (list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")
    for x in matrix:
            if type(x) not in (list) or len(x) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(x) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if type(y) not in (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(y / div, 2) for y in x] for x in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
