#!/usr/bin/python3
"""Multiplies two matrices with NumPy.

The product uses NumPy matrix multiplication.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return the NumPy product of two matrices.
    The matrices must be compatible for multiplication.
    """
    return numpy.matmul(m_a, m_b)
