#!/usr/bin/python3
""" Unittest for base.py """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setup(self):
        """ Resets the number of objects """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ tests id """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_id_set(self):
        """ tests id """
        b1 = Base(5)
        self.assertEqual(b1.id, 5)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(7)
        self.assertEqual(b3.id, 7)

    def test_id_assign(self):
        """ tests id """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_id_increment(self):
        """ tests id """
        b1 = Base(100)
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    if __name__ == '__main__':
        unittest.main()
