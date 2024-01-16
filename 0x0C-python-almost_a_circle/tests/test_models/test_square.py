#!/usr/bin/python3
"""unit test for square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_square(unittest.TestCase):
    """test for square class"""

    def test_class(self):
        """test Square class type"""
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")


if __name__ == "__main__":
    unittest.main()
