#!/usr/bin/python3
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """Test for instantiation of the Base Class"""

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id(self):
        b = Base(12)
        b.id = 17
        self.assertEqual(b.id, 17)

    def test_float_type(self):
        self.assertEqual(6.7, Base(6.7).id)
    
    def test_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(39).__nb__instances)

    def test_after_id_assignment(self):
        b = Base()
        b1 = Base(45)
        b2 = Base()
        self.assertEqual(b.id, b2.id - 1)

    def test_counter_increase(self):
        b = Base()
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base(6)
        b6 = Base()
        self.assertEqual(b.id, b6.id - 5)

    def test_string_input(self):
        self.assertEqual('Jared', Base('Jared').id)

    def test_set_numbers(self):
        self.assertEqual({1, 3, 5}, Base({1, 3, 5}).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_bool(self):
        self.assertEqual(False, Base(False).id)

    def test_range(self):
        self.assertEqual(range(10), Base(range(10)).id)

    def test_tuple(self):
        self.assertEqual((1, 4), Base((1, 4)).id)

    def test_complex(self):
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_memoryview(self):
        self.assertEqual(memoryview(b'abc'), Base(memoryview(b'abc')).id)

    def test_more_than_one_args(self):
        with self.assertRaises(TypeError):
            Base(3, 5, 7, 8)

    def test_is_no_instance(self):
        self.assertNotIsInstance(id, Base)

    def test_list(self):
        self.assertEqual([1, 2, 5], Base([1, 2, 5]).id)

    def test_bytes(self):
        self.assertEqual(b'jared', Base(b'jared').id)

if __name__ == '__main__':
    uniitest.main()
