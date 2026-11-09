#!/usr/bin/python3
"""Module that defines a rectangle with area and string output."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that can report its area and its dimensions."""

    def __init__(self, width, height):
        """Store width and height after validating both values.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description with width and height."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
