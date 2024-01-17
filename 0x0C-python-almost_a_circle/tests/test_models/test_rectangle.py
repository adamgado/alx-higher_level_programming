#!/usr/bin/python3
"""unit tests for rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout
import io


class Test_Rectangle(unittest.TestCase):
    """tests for rectangle class"""

    def test_class(self):
        """test Rectangle class type"""
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_subclass(self):
        """test if rectangle inherits base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_fewargs(self):
        """test too few arguments initialization"""
        with self.assertRaises(TypeError) as e:
            rect = Rectangle()
        a = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), a)

    def test_manyargs(self):
        """test too many arguments initialization"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(e.exception), s)

    def test_initialization(self):
        """test correct initialization"""
        Base._Base__nb_objects = 0
        a = Rectangle(1, 2)
        self.assertEqual(str(type(a)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(a, Base))
        b = {'_Rectangle__height': 2, '_Rectangle__width': 1,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(a.__dict__, b)

    def test_width_typeerror(self):
        """test width type error"""
        with self.assertRaises(TypeError) as e:
            a = Rectangle("x", 5)
        err = "width must be an integer"
        self.assertEqual(str(e.exception), err)

    def test_height_typeerror(self):
        """test height type error"""
        with self.assertRaises(TypeError) as e:
            a = Rectangle(5, "x")
        err = "height must be an integer"
        self.assertEqual(str(e.exception), err)

    def test_x_typeerror(self):
        """test x type error"""
        with self.assertRaises(TypeError) as e:
            a = Rectangle(2, 4, "x")
        err = "x must be an integer"
        self.assertEqual(str(e.exception), err)

    def test_y_typeerror(self):
        """test y type error"""
        with self.assertRaises(TypeError) as e:
            a = Rectangle(2, 4, 1, "x")
        err = "y must be an integer"
        self.assertEqual(str(e.exception), err)

    def test_width_valueerror(self):
        """test width value error"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(-2, 4)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

    def test_height_valueerror(self):
        """test height value error"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(2, -4)
        err = "height must be > 0"
        self.assertEqual(str(e.exception), err)

    def test_x_valueerror(self):
        """test x value error"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(2, 4, -1)
        err = "x must be >= 0"
        self.assertEqual(str(e.exception), err)

    def test_y_valueerror(self):
        """test y value error"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(2, 4, 1, -2)
        err = "y must be >= 0"
        self.assertEqual(str(e.exception), err)

    def test_size_with_position(self):
        """test all 4 arguments with no errors"""
        Base._Base__nb_objects = 0
        a = Rectangle(2, 4, 1, 2)
        b = {'_Rectangle__width': 2, '_Rectangle__height': 4,
             '_Rectangle__x': 1, '_Rectangle__y': 2, 'id': 1}
        self.assertEqual(a.__dict__, b)

    def test_keyword(self):
        """test keword arguments"""
        a = Rectangle(2, 4, x= 1, id=5, y=2)
        b = {'_Rectangle__width': 2, '_Rectangle__height': 4,
             '_Rectangle__x': 1, '_Rectangle__y': 2, 'id': 5}
        self.assertEqual(a.__dict__, b)

    def test_id(self):
        """test id number"""
        Base._Base__nb_objects = 5
        a = Rectangle(2, 4)
        self.assertEqual(a.id, 6)

    def test_attributes(self):
        """test properties"""
        Base._Base__nb_objects = 0
        a = Rectangle(2, 4)
        a.width = 5
        a.height = 10
        a.x = 1
        a.y = 2
        b = {'_Rectangle__width': 5, '_Rectangle__height': 10,
             '_Rectangle__x': 1, '_Rectangle__y': 2, 'id': 1}
        self.assertEqual(a.__dict__, b)
        self.assertEqual(a.width, 5)
        self.assertEqual(a.height, 10)
        self.assertEqual(a.x, 1)
        self.assertEqual(a.y, 2)

    def test_xy_default(self):
        """test position default """
        a = Rectangle(2, 4)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)

    def test_area(self):
        """test area"""
        a = Rectangle(2, 4)
        self.assertEqual(a.area(), 8)

    def test_area_extra(self):
        """test area with other arguments"""
        a = Rectangle(2, 4, 1, 2, 5)
        self.assertEqual(a.area(), 8)

    def test_display_one(self):
        """test display one by one"""
        a = Rectangle(1, 1)
        printed = io.StringIO()
        with redirect_stdout(printed):
            a.display()
        shape = "#\n"
        self.assertEqual(printed.getvalue(), shape)

    def test_display_basic(self):
        """test display basic"""
        a = Rectangle(2, 4)
        printed = io.StringIO()
        with redirect_stdout(printed):
            a.display()
        shape = """##
##
##
##
"""
        self.assertEqual(printed.getvalue(), shape)

    def test_display_position(self):
        """test display with positions"""
        a = Rectangle(2, 4, 1, 2)
        printed = io.StringIO()
        with redirect_stdout(printed):
            a.display()
        shape = """

 ##
 ##
 ##
 ##
"""
        self.assertEqual(printed.getvalue(), shape)

    def test_str(self):
        """test __str__"""
        Base._Base__nb_objects = 0
        a = Rectangle(2, 4, 1, 2)
        b = '[Rectangle] (1) 1/2 - 2/4'
        self.assertEqual(str(a), b)

    def test_update_nochange(self):
        """test update without arguments"""
        a = Rectangle(2, 4)
        b = a.__dict__.copy()
        a.update()
        self.assertEqual(a.__dict__, b)

    def test_update_each(self):
        """test update each value at a time"""
        a = Rectangle(1, 1, 1, 1, 1)
        b = a.__dict__.copy()
        a.update(9)
        b["id"] = 9
        self.assertEqual(a.__dict__, b)

        a.update(9, 2, 1, 1, 1)
        b["_Rectangle__width"] = 2
        self.assertEqual(a.__dict__, b)

        a.update(9, 2, 4, 1, 1)
        b["_Rectangle__height"] = 4
        self.assertEqual(a.__dict__, b)

        a.update(9, 2, 4, 3, 1)
        b["_Rectangle__x"] = 3
        self.assertEqual(a.__dict__, b)

        a.update(9, 2, 4, 3, 6)
        b["_Rectangle__y"] = 6
        self.assertEqual(a.__dict__, b)

    def test_update_together(self):
        """test update all values at once"""
        a = Rectangle(7, 7, 7, 7, 7)
        a.update(1, 2, 3, 4, 5)
        self.assertEqual(str(a), "[Rectangle] (1) 4/5 - 2/3")

    def test_update_error(self):
        """test update error"""
        a = Rectangle(2, 4)
        with self.assertRaises(ValueError) as e:
            a.update(2, -4)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

    def test_update_kwargs(self):
        """test update with keyword arguments out of order"""
        a = Rectangle(1, 2, 3, 4, 5)
        b = a.__dict__.copy()
        a.update(y=10, id=2, height=6, x=8, width=4)
        b["id"] = 2
        b["_Rectangle__width"] = 4
        b["_Rectangle__height"] = 6
        b["_Rectangle__x"] = 8
        b["_Rectangle__y"] = 10
        self.assertEqual(a.__dict__, b)

    def test_update_id(self):
        """test update that object id stays the same with update"""
        Base._Base__nb_objects = 0
        a = Rectangle(1, 2, 3, 4)
        b = a.__dict__.copy()
        a.update(width=4)
        b["_Rectangle__width"] = 4
        self.assertEqual(a.__dict__, b)

    def test_to_dictionary(self):
        """test to_dictionary"""
        a = Rectangle(2, 4, 1, 2, 10)
        b = {'id': 10, 'width': 2, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(a.to_dictionary(), b)


if __name__ == "__main__":
    unittest.main()
