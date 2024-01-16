#!/usr/bin/python3
"""unit test for rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """test for rectangle class"""

    def test_class(self):
        """test rectangle class type"""
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")


if __name__ == "__main__":
    unittest.main()
