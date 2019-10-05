#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_repeatmax(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 4]), 4)

    def test_negativevalues(self):
        self.assertEqual(max_integer([-5, -4, -5, -4, -1]), -1)

    def test_negativevaluesandzero(self):
        self.assertEqual(max_integer([0, 0, 0, 0, -1]), 0)

    def test_stringslist(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_onlyonevalue(self):
        self.assertEqual(max_integer([5]), 5)

if __name__ == '__main__':
    unittest.main()
