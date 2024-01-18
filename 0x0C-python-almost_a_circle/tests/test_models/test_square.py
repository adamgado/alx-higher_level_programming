#!/usr/bin/python3
"""unit tests for square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
import io


class Test_class(unittest.TestCase):
    """test the square class"""

    def test_class(self):
        """test square class type"""
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_sublcass(self):
        """test if Square inherits rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_double_sublcass(self):
        """test if Square inherits base"""
        self.assertTrue(issubclass(Square, Base))

    def test_fewargs(self):
        """test too few arguments error"""
        with self.assertRaises(TypeError) as e:
            a = Square()
        err = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), err)

    def test_manyargs(self):
        """test too many arguments error"""
        with self.assertRaises(TypeError) as e:
            a = Square(1, 2, 3, 4, 5)
        err = "__init__() takes from 2 to 5 positional arguments \
but 6 were given"
        self.assertEqual(str(e.exception), err)

    def test_size(self):
        """test that size argument is width and height"""
        Base._Base__nb_objects = 0
        a = Square(5)
        b = {'_Rectangle__width': 5, '_Rectangle__height': 5,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(a.__dict__, b)

    def test_size_typeerror(self):
        """test size type error"""
        with self.assertRaises(TypeError) as e:
            a = Square("g")
        err = "width must be an integer"
        self.assertEqual(str(e.exception), err)

    def test_x_typeerror(self):
        """test x type error"""
        with self.assertRaises(TypeError) as e:
            a = Square(1, "g")
        err = "x must be an integer"
        self.assertEqual(str(e.exception), err)

    def test_y_typeerror(self):
        """test y type error"""
        with self.assertRaises(TypeError) as e:
            a = Square(1, 2, "g")
        err = "y must be an integer"
        self.assertEqual(str(e.exception), err)

    def test_size_valueerror(self):
        """test size value error"""
        with self.assertRaises(ValueError) as e:
            a = Square(-1)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

    def test_size_zero(self):
        """test size zero error"""
        with self.assertRaises(ValueError) as e:
            a = Square(0)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

    def test_x_valueerror(self):
        """test x value error"""
        with self.assertRaises(ValueError) as e:
            a = Square(1, -2)
        err = "x must be >= 0"
        self.assertEqual(str(e.exception), err)

    def test_y_valueerror(self):
        """test y value error"""
        with self.assertRaises(ValueError) as e:
            a = Square(1, 2, -3)
        err = "y must be >= 0"
        self.assertEqual(str(e.exception), err)

    def test_size_xy(self):
        """test size and positional arguments"""
        Base._Base__nb_objects = 0
        a = Square(1, 2, 3)
        b = {'_Rectangle__width': 1, '_Rectangle__height': 1,
             '_Rectangle__x': 2, '_Rectangle__y': 3, 'id': 1}
        self.assertEqual(a.__dict__, b)

    def test_size_xy_id(self):
        """test size and positional and id arguments"""
        a = Square(1, 2, 3, 5)
        b = {'_Rectangle__width': 1, '_Rectangle__height': 1,
             '_Rectangle__x': 2, '_Rectangle__y': 3, 'id': 5}
        self.assertEqual(a.__dict__, b)

    def test_keyword_args(self):
        """test initialization with keywords out of order"""
        a = Square(1, id=5, y=3, x=2)
        b = {'_Rectangle__width': 1, '_Rectangle__height': 1,
             '_Rectangle__x': 2, '_Rectangle__y': 3, 'id': 5}
        self.assertEqual(a.__dict__, b)

    def test_id_increase(self):
        """test if id increases with base id"""
        Base._Base__nb_objects = 9
        a = Square(5)
        self.assertEqual(a.id, 10)

    def test_attributes(self):
        """test properties"""
        Base._Base__nb_objects = 0
        a = Square(5, 10)
        a.size = 2
        a.x = 1
        a.y = 3
        b = {'_Rectangle__width': 2, '_Rectangle__height': 2,
             '_Rectangle__x': 1, '_Rectangle__y': 3, 'id': 1}
        self.assertEqual(a.__dict__, b)
        self.assertEqual(a.size, 2)
        self.assertEqual(a.x, 1)
        self.assertEqual(a.y, 3)

    def test_area(self):
        """test area"""
        a = Square(6, 2, 3, 5)
        self.assertEqual(a.area(), 36)

    def test_display_one(self):
        """test display one by one"""
        a = Square(1)
        printed = io.StringIO()
        with redirect_stdout(printed):
            a.display()
        shape = "#\n"
        self.assertEqual(printed.getvalue(), shape)

    def test_display_basic(self):
        """test display size only"""
        a = Square(2)
        printed = io.StringIO()
        with redirect_stdout(printed):
            a.display()
        shape = """##
##
"""
        self.assertEqual(printed.getvalue(), shape)

    def test_display_position(self):
        """test display with xy positions"""
        a = Square(5, 1, 3)
        printed = io.StringIO()
        with redirect_stdout(printed):
            a.display()
        shape = """


 #####
 #####
 #####
 #####
 #####
"""
        self.assertEqual(printed.getvalue(), shape)

    def test_str(self):
        """test __str__"""
        a = Square(5, 1, 2, 10)
        string = '[Square] (10) 1/2 - 5'
        self.assertEqual(str(a), string)

    def test_update_nochange(self):
        """test update with no arguments"""
        a = Square(1, 2)
        b = a.__dict__.copy()
        a.update()
        self.assertEqual(a.__dict__, b)

    def test_update_error(self):
        """test update error"""
        a = Square(2, 5)
        with self.assertRaises(ValueError) as e:
            a.update(2, -5)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

    def test_update_args(self):
        """test update with args"""
        a = Square(1, 1, 1, 1)
        b = a.__dict__.copy()
        a.update(5, 2, 3, 4)
        b["_Rectangle__height"] = 2
        b["_Rectangle__width"] = 2
        b["_Rectangle__x"] = 3
        b["_Rectangle__y"] = 4
        b["id"] = 5
        self.assertEqual(a.__dict__, b)

    def test_update_kwargs(self):
        """test update keyword args"""
        a = Square(5)
        b = a.__dict__.copy()
        a.update(y=4, id=5, x=3, size=2)
        b["_Rectangle__y"] = 4
        b["id"] = 5
        b["_Rectangle__x"] = 3
        b["_Rectangle__width"] = 2
        b["_Rectangle__height"] = 2
        self.assertEqual(a.__dict__, b)

    def test_to_dictionary(self):
        """test to_dictionary"""
        a = Square(1, 2, 3, 4)
        dict = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(a.to_dictionary(), dict)
        a_dict = a.to_dictionary()
        b = Square(1, 1)
        b.update(**a_dict)
        self.assertEqual(str(a), str(b))
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()
