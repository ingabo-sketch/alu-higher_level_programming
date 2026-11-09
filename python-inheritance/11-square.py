#!/usr/bin/python3
"""Module that defines a square with its own string description."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square that prints itself as a square rather than a rectangle."""

    def __init__(self, size):
        """Store size after checking that it is a positive integer.

        Args:
            size (int): Length of every side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description with its size."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
