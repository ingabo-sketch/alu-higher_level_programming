#!/usr/bin/python3
"""Module that defines a Square comparable by area."""


class Square:
    """Represent a square that can be compared by its area."""

    def __init__(self, size=0):
        """Initialize a square and validate its size.

        Args:
            size (int or float): The size of the square.
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
            value (int or float): The new size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than zero.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return whether two squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return whether two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return whether this square is smaller than another."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return whether this square is smaller than or equal to another."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return whether this square is larger than another."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return whether this square is larger than or equal to another."""
        return self.area() >= other.area()
