#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
    class for testing
    '''
    def test_output(self):
        '''
        correct output
        '''
        self.assertEqual(max_integer([3, 3, 3, 10]), 10)
        self.assertEqual(max_integer([6, 4]), 6)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([22, 4, 4, 3]), 22)
        self.assertEqual(max_integer([47, 4]), 47)

    def test_empty(self):
        '''
        test with empty input
        '''
        self.assertEqual(max_integer([]), None)

    def test_no_list(self):
        '''
        with no line
        '''
        self.assertEqual(max_integer(), None)

    def test_int_str(self):
        '''
        string and int
        '''
        with self.assertRaises(TypeError):
            max_integer([3, 10, 3, "amine"])

    def test_int(self):
        '''
        signed and unsigned number
        '''
        self.assertEqual(max_integer([-3, 4, -9, -1, -5]), 4)
        self.assertEqual(max_integer([2, 3, 10, 12, 3]), 12)
        self.assertEqual(max_integer([1, 3, 5, -3, -5]), 5)
