#!/usr/bin/python3
"""Module that defines a geometry base class with an integer validator."""


class BaseGeometry:
    """Base class that validates integers and leaves area unimplemented."""

    def area(self):
        """Raise an exception because area is not implemented.

        Raises:
            Exception: Always, with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than zero.

        Args:
            name (str): Name of the value, used in the error message.
            value (int): Value that must be a positive integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
