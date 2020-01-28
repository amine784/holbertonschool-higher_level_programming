#!/usr/bin/python3
"""
unitest
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    tes class
    """
    def test_base(self):
        """
        exple of testing
        """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(14)
        self.assertEqual(b3.id, 14)
        b4 = Base(None)
        self.assertEqual(b4.id, 3)
        b5 = Base(5)
        self.assertEqual(b5.id, 5)
        b6 = Base(30)
        self.assertEqual(b6.id, 30)
        b7 = Base()
        self.assertEqual(b7.id, 4)
