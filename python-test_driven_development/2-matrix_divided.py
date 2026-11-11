#!/usr/bin/python3
"""Divides every element of a matrix.

The function returns a new matrix and leaves the original unchanged.
Each result is rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """Divide every matrix element by div and return a new matrix.
    Rows must share one size and every value must be a number.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(message)
    row_size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(message)
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(message)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
