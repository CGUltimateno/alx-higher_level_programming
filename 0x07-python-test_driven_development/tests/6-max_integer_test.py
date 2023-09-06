#!/usr/bin/python3
"""unitest for max_integer"""
import unittest

max_integer = __import__('6-max_integer.py').max_integer


class Test(unittest.TestCase):
    def test_first(self):
        res = max_integer([3, 4, 5, 6, 2])
        self.assertEqual(res, 6)

    def test_second(self):
        res = max_integer([4, 4, 2])
        self.assertEqual(res, 4)

    def test_third(self):
        res = max_integer([-200, -44, -77])
        self.assertEqual(res, -44)

    def test_invalid_element(self):
        with self.assertRaises(TypeError):
            max_integer(['a', '2', None, 3.23])

    def test_empty_list(self):
        res = max_integer([])
        self.assertEqual(res, None)

    if __name__ == '__main__':
        unittest.main()
