#!/usr/bin/python3
"""Defines the tests for models/rectangle.py module"""
import sys
import unittest
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectanble_Instantiation(unittest.TestCase):
    """Tests for instatiation of the Rectangle class"""

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
    
    def test_2_args(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 8)
        self.assertEqual(r1.id, r2.id - 1)

if __name__  == '__main__':
    unittest.main()
