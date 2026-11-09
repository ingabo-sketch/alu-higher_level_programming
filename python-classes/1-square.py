#!/usr/bin/python3
"""Module that defines a Square by its private size."""


class Square:
    """Represent a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a square with a given size.

        Args:
            size: The size of the square.
        """
        self.__size = size
