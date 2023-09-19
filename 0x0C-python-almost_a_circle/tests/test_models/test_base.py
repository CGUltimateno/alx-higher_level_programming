#!/usr/bin/python3
""" Unittest for base.py """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        Base.__nb_objects = 0

    def test_default_id_assignment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id_assignment(self):
        b1 = Base(12)
        b2 = Base(40)
        b3 = Base(99)

        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 40)
        self.assertEqual(b3.id, 99)

    def test_mixed_id_assignment(self):
        b1 = Base()
        b2 = Base(50)
        b3 = Base()

        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 50)
        self.assertEqual(b3.id, 6)

    def test_id_increment_after_custom_id(self):
        b1 = Base(100)
        b2 = Base()

        self.assertEqual(b1.id, 100)
        self.assertEqual(b2.id, 4)


if __name__ == "__main__":
    unittest.main()
