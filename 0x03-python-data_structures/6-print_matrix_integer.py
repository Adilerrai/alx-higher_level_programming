#!/usr/bin/python3


def print_matrix_integer(matrix=None):
    if matrix is not None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=' ')
            print()