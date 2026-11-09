#!/usr/bin/python3
"""Module that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle with n rows.

    Args:
        n (int): Number of rows to build.

    Returns:
        list: Rows of the triangle, or an empty list when n is not positive.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for row_index in range(1, n):
        previous = triangle[-1]
        row = [1]
        for column in range(1, row_index):
            row.append(previous[column - 1] + previous[column])
        row.append(1)
        triangle.append(row)
    return triangle
