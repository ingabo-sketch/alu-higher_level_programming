#!/usr/bin/python3
"""Unit tests for the Base class."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test id management and serialization on Base."""

    def tearDown(self):
        """Remove files created while a test was running."""
        for name in (
            "Base.json", "Rectangle.json", "Square.json",
            "Base.csv", "Rectangle.csv", "Square.csv"
        ):
            if os.path.exists(name):
                os.remove(name)

    def test_id_increments_when_missing(self):
        """Assign the next id when the caller omits it."""
        first = Base()
        second = Base()
        self.assertEqual(second.id, first.id + 1)

    def test_id_keeps_given_value(self):
        """Keep an id that the caller provides."""
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_id_continues_after_manual_id(self):
        """Keep counting after an instance is given its own id."""
        before = Base()
        Base(12)
        after = Base()
        self.assertEqual(after.id, before.id + 1)

    def test_to_json_string_none_and_empty(self):
        """Return an empty JSON list for missing or empty input."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Return a JSON string for a list of dictionaries."""
        dictionary = {"id": 1, "width": 2}
        text = Base.to_json_string([dictionary])
        self.assertIsInstance(text, str)
        self.assertEqual(json.loads(text), [dictionary])

    def test_from_json_string_none_and_empty(self):
        """Return an empty list for a missing or empty JSON string."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_list(self):
        """Decode a JSON list of dictionaries."""
        source = [{"id": 89, "width": 10}, {"id": 7, "width": 1}]
        text = Base.to_json_string(source)
        self.assertEqual(Base.from_json_string(text), source)

    def test_save_to_file_none_and_empty(self):
        """Write an empty JSON list when there are no objects."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_rectangles(self):
        """Write every rectangle dictionary into Rectangle.json."""
        first = Rectangle(10, 7, 2, 8, 1)
        second = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([first, second])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            loaded = json.loads(file.read())
        self.assertEqual(
            loaded, [first.to_dictionary(), second.to_dictionary()]
        )

    def test_save_to_file_overwrites(self):
        """Replace an existing JSON file on the next save."""
        Rectangle.save_to_file([Rectangle(1, 1, 0, 0, 1)])
        Rectangle.save_to_file([Rectangle(3, 4, 0, 0, 9)])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            loaded = json.loads(file.read())
        self.assertEqual(loaded[0]["id"], 9)
        self.assertEqual(loaded[0]["width"], 3)

    def test_create_rectangle(self):
        """Build a rectangle from a dictionary of attributes."""
        original = Rectangle(3, 5, 1, 2, 8)
        created = Rectangle.create(**original.to_dictionary())
        self.assertIsNot(original, created)
        self.assertEqual(str(original), str(created))

    def test_create_square(self):
        """Build a square from a dictionary of attributes."""
        original = Square(4, 2, 3, 11)
        created = Square.create(**original.to_dictionary())
        self.assertIsInstance(created, Square)
        self.assertEqual(str(original), str(created))

    def test_load_from_file_missing(self):
        """Return an empty list when the JSON file does not exist."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertFalse(os.path.exists("Rectangle.json"))

    def test_load_from_file_rectangle_and_square(self):
        """Reload rectangles and squares as new instances."""
        rectangles = [Rectangle(10, 7, 2, 8, 1), Rectangle(2, 4, 0, 0, 2)]
        Rectangle.save_to_file(rectangles)
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(
            [str(item) for item in loaded_rectangles],
            [str(item) for item in rectangles]
        )
        self.assertIsNot(loaded_rectangles[0], rectangles[0])
        squares = [Square(5, 0, 0, 5), Square(7, 9, 1, 6)]
        Square.save_to_file(squares)
        loaded_squares = Square.load_from_file()
        self.assertTrue(
            all(isinstance(item, Square) for item in loaded_squares)
        )
        self.assertEqual(
            [str(item) for item in loaded_squares],
            [str(item) for item in squares]
        )

    def test_csv_round_trip(self):
        """Save and load rectangles and squares through CSV files."""
        rectangles = [Rectangle(10, 7, 2, 8, 1), Rectangle(2, 4, 0, 0, 2)]
        Rectangle.save_to_file_csv(rectangles)
        loaded_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(
            [item.to_dictionary() for item in loaded_rectangles],
            [item.to_dictionary() for item in rectangles]
        )
        Square.save_to_file_csv(None)
        self.assertEqual(Square.load_from_file_csv(), [])
        squares = [Square(5, 1, 2, 3)]
        Square.save_to_file_csv(squares)
        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(
            loaded_squares[0].to_dictionary(), squares[0].to_dictionary()
        )

    def test_load_csv_missing(self):
        """Return an empty list when the CSV file does not exist."""
        self.assertEqual(Square.load_from_file_csv(), [])
