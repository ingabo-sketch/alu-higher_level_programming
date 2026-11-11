#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max integer function."""

    def test_ordered_list(self):
        """Test a list sorted in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list with the largest value in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list whose largest value is first."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        """Test a list that contains one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list made only of negative integers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_signs(self):
        """Test a list of negative and positive integers."""
        self.assertEqual(max_integer([-10, 0, 5, 2]), 5)

    def test_identical_values(self):
        """Test a list where every element is the same."""
        self.assertEqual(max_integer([2, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
