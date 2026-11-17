#!/usr/bin/python3
"""Unit tests for the Square class."""
import io
import unittest
from contextlib import redirect_stdout
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test construction, size, and serialization for Square."""

    def test_constructor_area_and_display(self):
        """Build a square, compute its area, and print it."""
        square = Square(5, 0, 0, 1)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 5")
        self.assertEqual(square.area(), 25)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        output = io.StringIO()
        with redirect_stdout(output):
            square.display()
        self.assertEqual(output.getvalue(), "#####\n" * 5)
        offset = Square(2, 2, 0, 2)
        output = io.StringIO()
        with redirect_stdout(output):
            offset.display()
        self.assertEqual(output.getvalue(), "  ##\n  ##\n")
        lowered = Square(3, 1, 3, 3)
        output = io.StringIO()
        with redirect_stdout(output):
            lowered.display()
        self.assertEqual(output.getvalue(), "\n\n\n ###\n ###\n ###\n")

    def test_plain_square_keeps_its_size(self):
        """Keep the given size when position and id are omitted."""
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.area(), 25)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_constructor_rejects_bad_values(self):
        """Reject a bad size or position when the square is created."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("9")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 0, "3")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1)

    def test_size_getter_and_setter(self):
        """Change both sides together and keep the width error text."""
        square = Square(5, 0, 0, 1)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(str(square), "[Square] (1) 0/0 - 10")
        self.assertEqual(square.height, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.size = "9"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.size = 0
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, True)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 0, -1)

    def test_update_args_and_kwargs(self):
        """Apply positional size updates and keyword updates."""
        square = Square(5, 0, 0, 1)
        square.update(10)
        self.assertEqual(str(square), "[Square] (10) 0/0 - 5")
        square.update(1, 2)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 2")
        square.update(1, 2, 3)
        self.assertEqual(str(square), "[Square] (1) 3/0 - 2")
        square.update(1, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")
        square.update(x=12)
        self.assertEqual(str(square), "[Square] (1) 12/4 - 2")
        square.update(size=7, y=1)
        self.assertEqual(str(square), "[Square] (1) 12/1 - 7")
        square.update(size=7, id=89, y=1)
        self.assertEqual(str(square), "[Square] (89) 12/1 - 7")
        square.update(4, 3, 2, 1, size=9)
        self.assertEqual(str(square), "[Square] (4) 2/1 - 3")

    def test_to_dictionary(self):
        """Return id, size, x, and y, then apply that dictionary."""
        square = Square(10, 2, 1, 1)
        dictionary = square.to_dictionary()
        self.assertEqual(dictionary, {"id": 1, "size": 10, "x": 2, "y": 1})
        self.assertNotIn("width", dictionary)
        other = Square(1, 1, 0, 2)
        other.update(**dictionary)
        self.assertEqual(str(other), str(square))
        self.assertFalse(square == other)
