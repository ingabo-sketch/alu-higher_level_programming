#!/usr/bin/python3
"""Module that defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square as a rectangle with equal sides."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size: The length of every side of the square.
            x: The horizontal offset of the square.
            y: The vertical offset of the square.
            id: The public id inherited from Base.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and the height to the same size.

        Args:
            value: The new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Assign new values to the square attributes.

        Args:
            args: Values in the order id, size, x, y.
            kwargs: Attribute names mapped to new values.
        """
        attributes = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
            return
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
