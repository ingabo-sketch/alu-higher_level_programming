#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import unittest
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test construction, validation, and output for Rectangle."""

    def test_constructor_and_area(self):
        """Store the given values and compute the area."""
        rectangle = Rectangle(3, 2, 1, 4, 12)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 4)
        self.assertEqual(rectangle.id, 12)
        self.assertEqual(rectangle.area(), 6)
        other = Rectangle(8, 7, 0, 0, 1)
        self.assertEqual(other.area(), 56)

    def test_default_position(self):
        """Use zero for x and y when they are omitted."""
        first = Rectangle(10, 2)
        second = Rectangle(2, 10)
        self.assertEqual(first.x, 0)
        self.assertEqual(first.y, 0)
        self.assertEqual(second.id, first.id + 1)

    def test_type_validation(self):
        """Reject values that are not integers, including booleans."""
        cases = (
            ("height", (10, "2")),
            ("width", ("10", 2)),
            ("x", (10, 2, {})),
            ("y", (10, 2, 3, 1.5)),
        )
        for name, args in cases:
            message = name + " must be an integer"
            with self.assertRaisesRegex(TypeError, message):
                Rectangle(*args)
        rectangle = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.width = True
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.x = None

    def test_value_validation(self):
        """Reject a non-positive size and a negative position."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 2, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)
        rectangle = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.width = -10
        rectangle.x = 0
        rectangle.y = 0
        self.assertEqual(rectangle.x, 0)

    def test_display_and_string(self):
        """Print the rectangle and return its string form."""
        output = io.StringIO()
        with redirect_stdout(output):
            Rectangle(2, 2, 0, 0, 1).display()
        self.assertEqual(output.getvalue(), "##\n##\n")
        output = io.StringIO()
        with redirect_stdout(output):
            Rectangle(2, 3, 2, 2, 1).display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n  ##\n")
        output = io.StringIO()
        with redirect_stdout(output):
            Rectangle(3, 2, 1, 0, 1).display()
        self.assertEqual(output.getvalue(), " ###\n ###\n")
        self.assertEqual(
            str(Rectangle(4, 6, 2, 1, 12)),
            "[Rectangle] (12) 2/1 - 4/6"
        )
        placed = Rectangle(5, 5, 1)
        self.assertEqual(
            str(placed),
            "[Rectangle] ({}) 1/0 - 5/5".format(placed.id)
        )

    def test_update_args_and_kwargs(self):
        """Apply positional updates first and keyword updates otherwise."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 10/10")
        rectangle.update(89, 2)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/10")
        rectangle.update(89, 2, 3)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/3")
        rectangle.update(89, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/10 - 2/3")
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")
        rectangle.update(height=1)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/1")
        rectangle.update(width=1, x=2)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 2/5 - 1/1")
        rectangle.update(y=1, width=2, x=3, id=7)
        self.assertEqual(str(rectangle), "[Rectangle] (7) 3/1 - 2/1")
        rectangle.update(1, 2, 3, 4, 5, id=9, width=8)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 4/5 - 2/3")

    def test_to_dictionary(self):
        """Return every public attribute and apply that dictionary."""
        rectangle = Rectangle(10, 2, 1, 9, 1)
        dictionary = rectangle.to_dictionary()
        self.assertEqual(
            dictionary,
            {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        )
        other = Rectangle(1, 1, 0, 0, 2)
        other.update(**dictionary)
        self.assertEqual(str(other), str(rectangle))
        self.assertIsNot(other, rectangle)
        self.assertFalse(rectangle == other)
