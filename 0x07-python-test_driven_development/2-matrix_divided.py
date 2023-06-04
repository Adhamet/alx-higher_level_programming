#!/usr/bin/python3
'''
This module does matrix division
'''


def matrix_divided(matrix, div):
    '''returns a new matrix after division'''

    rw_l = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msg)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError(msg)
        rw_l.append(len(row))
    if len(set(rw_l)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif int(div) == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(
        lambda row: list(map(
            lambda x: round(x/div, 2), row
        )), matrix
    ))

    return new_matrix
