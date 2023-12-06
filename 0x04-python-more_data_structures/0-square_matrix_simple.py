#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if len(matrix) > 0:
        for a in matrix[:]:
            new_matrix.append(list(map(lambda x: x * x, row)))
    return new_matrix
