#!/usr/bin/python3
"""Module that defines a Square that can print itself."""


class Square:
    """Represent a square that can be printed with the # character."""

    def __init__(self, size=0):
        """Initialize a square and validate its size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
