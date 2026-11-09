#!/usr/bin/python3
"""Module that defines a list which can print itself sorted."""


class MyList(list):
    """List subclass that can print its values in ascending order."""

    def print_sorted(self):
        """Print the list values in ascending order without changing them."""
        print(sorted(self))
