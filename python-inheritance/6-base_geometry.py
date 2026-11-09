#!/usr/bin/python3
"""Module that defines a geometry base class with an area method."""


class BaseGeometry:
    """Base class whose area method is not implemented yet."""

    def area(self):
        """Raise an exception because area is not implemented.

        Raises:
            Exception: Always, with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")
