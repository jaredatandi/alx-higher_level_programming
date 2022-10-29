#!/usr/bin/python3
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """Test for instantiation of the Base Class"""

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

if __name__ == '__main__':
    uniitest.main()
