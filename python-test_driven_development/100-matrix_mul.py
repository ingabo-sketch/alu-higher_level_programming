#!/usr/bin/python3
"""Multiplies two matrices.

Both matrices are validated before the product is calculated.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices and return the product.
    Each matrix must be a non-empty rectangle of numbers.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if any(type(row) is not list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(row) is not list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(
                    "m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(
                    "m_b should contain only integers or floats")
    row_size = len(m_a[0])
    for row in m_a:
        if len(row) != row_size:
            raise TypeError("each row of m_a must be of the same size")
    row_size = len(m_b[0])
    for row in m_b:
        if len(row) != row_size:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    product = []
    for row in m_a:
        new_row = []
        for column in range(len(m_b[0])):
            total = 0
            for index in range(len(m_b)):
                total += row[index] * m_b[index][column]
            new_row.append(total)
        product.append(new_row)
    return product
