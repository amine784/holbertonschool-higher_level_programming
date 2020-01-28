#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def values_id(self):
        r = Rectangle(1, 1, 0, 0)
            self.assertEqual(r.width, 1)
            self.assertEqual(r.height, 1)
            self.assertEqual(r.x, 0)
            self.assertEqual(r.y, 0)
            self.assertEqual(r.id, 1)

        r = Rectangle(1, 1, 0, 0)
            self.assertEqual(r.width, 1)
            self.assertEqual(r.height, 1)
            self.assertEqual(r.x, 0)
            self.assertEqual(r.y, 0)
            self.assertEqual(r.id, 2)

        r = Rectangle(1, 1, 1, 1, 12)
            self.assertEqual(r.width, 1)
            self.assertEqual(r.height, 1)
            self.assertEqual(r.x, 1)
            self.assertEqual(r.y, 1)
            self.assertEqual(r.id, 12)

    def test_type_values(self):
        typ = (8, [3], '4', 1)
        self.assertRaises(TypeError, Rectangle, typ)
        typ = ('1', 2, 0, 1)
        self.assertRaises(TypeError, Rectangle, typ)
        typ = ((1), 2, 0, 1)
        self.assertRaises(TypeError, Rectangle, typ)
        typ = ([1], 2, 0, 1)
        self.assertRaises(TypeError, Rectangle, typ)

    def test_value(self):
        val = [1, 1, 1, 1]
        self.assertRaises(ValueError, Rectangle, *val)
        val = [-2, 1, 1, 1]
        self.assertRaises(ValueError, Rectangle, *val)
        val = [2, 1, 1, -1]
        self.assertRaises(ValueError, Rectangle, *val)
        val = [2, 1, -1, 1]
        self.assertRaises(ValueError, Rectangle, *val)

    def test_value_area(self):
        r1 = Rectangle(2, 5)
        self.assertEqual(r1.area(), 10)
        self.assertNotEqual(r1.area(), 7)
        
        r2 = Rectangle(2, 4)
        self.assertEqual(r2.area(), 8)
        self.assertNotEqual(r2.area(), 6)
        
        r3 = Rectangle(2, 2, 0, 0, 24)
        self.assertEqual(r3.area(), 4)
        self.assertNotEqual(r3.area(), 24)
