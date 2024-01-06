#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer function"""
    def test_empty_list(self):
        """test empty list argument"""
        self.assertEqual(max_integer([]), None)

    def test_no_arg(self):
        """test no arguments"""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """test one element in list argument"""
        self.assertEqual(max_integer([2]), 2)

    def test_equal(self):
        """test all elements in the list are equal"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_basic(self):
        """test normal case"""
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_outoforder(self):
        """test out of order normal case"""
        self.assertEqual(max_integer([1, 3, 4, 2, 9, 5]), 9)

    def test_outoforder_large(self):
        """test out of order large list"""
        self.assertEqual(max_integer([33, 60, 90, 25, 3000, 80, 95,
                                     2020, 252, 505]), 3000)

    def test_positive_and_negative(self):
        """test positive and negative numbers together"""
        self.assertEqual(
            max_integer([-230, 5, 19, 25, -1000, 71, 90, 100, -250, -100]),
            100)

    def test_int_and_float(self):
        """test ints and floats together"""
        self.assertEqual(
            max_integer(
                [75, 99.8, -250, -0.5, 10, 100, -100000, 100.1]), 100.1)

    def test_number_string(self):
        """test a string of numbers"""
        self.assertEqual(max_integer("123459876"), "9")

    def test_char_string(self):
        """test a string of characters"""
        self.assertEqual(max_integer("happy town"), "y")

    def test_str_list(self):
        """test list of strings of characters"""
        self.assertEqual(
            max_integer([["abc"], ["xyz"], ["wuf"], ["lap"], ["dog"]]),
            ["xyz"])

    def test_list_of_lists(self):
        """test a list of lists"""
        self.assertEqual(max_integer([[], [2], [4], [2, 5]]), [4])

    def test_mixed_list(self):
        """test list of different types"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 5], 100, "x"])

    def test_dictionaries(self):
        """test for a list of dictionaries"""
        with self.assertRaises(TypeError):
            max_integer([{20: 25, 15: 45}, {"x": "y"}])

    def test_int(self):
        """test for int argument"""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == '__main__':
    unittest.main()
