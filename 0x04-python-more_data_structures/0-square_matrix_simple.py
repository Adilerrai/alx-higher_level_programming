#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rows in matrix:
        new_row = []
        for columns in rows:
            j = columns ** 2
            new_row.append(j)
        new_matrix.append(new_row)
    return new_matrix
