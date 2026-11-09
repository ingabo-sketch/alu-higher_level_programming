#!/usr/bin/python3
"""Module that defines an integer with inverted comparisons."""


class MyInt(int):
    """Integer that treats equality and inequality as opposites."""

    def __eq__(self, other):
        """Return True when the values are not equal.

        Args:
            other (object): Value compared with this integer.

        Returns:
            bool: The inverted equality result.
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return True when the values are equal.

        Args:
            other (object): Value compared with this integer.

        Returns:
            bool: The inverted inequality result.
        """
        return int.__eq__(self, other)
