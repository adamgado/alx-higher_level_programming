#!/usr/bin/python3
"""base unit test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class Test_Base(unittest.TestCase):
    """Tests for class Base """

    def test_base_instance(self):
        """test Base initialization"""
        a = Base()
        self.assertEqual(str(type(a)), "<class 'models.base.Base'>")
        self.assertEqual(a.id, 1)

    def test_two_arguments(self):
        """tests initialization with 2 arguments after self"""
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        err = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), err)

    def test_ids_order(self):
        """test ids in order of initialization"""
        a = Base()
        b = Base()
        self.assertEqual(a.id + 1, b.id)

    def test_id_int(self):
        """test int id"""
        a = 98
        b = Base(a)
        self.assertEqual(b.id, a)

    def test_id_string(self):
        """test string id"""
        a = "x"
        b = Base(a)
        self.assertEqual(b.id, a)

    def test_id_keyword(self):
        """test keyword argument id"""
        a = 5
        b = Base(id=a)
        self.assertEqual(b.id, a)

    def test_tojsonstring_noargs(self):
        """test to_json_string() static method with 0 arguments"""
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        a = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), a)

    def test_tojsonstring_emptylist(self):
        """test to_json_string with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_tojsonstring_length(self):
        """test to_json_string returns string of correct length"""
        a = [{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}]
        self.assertEqual(len(Base.to_json_string(a)),
                         len(str(a)))

    def test_tojsonstring_stringisdict(self):
        """test to_json_string returns string of dictionary"""
        a = [{"x": 5}]
        self.assertEqual(Base.to_json_string(a), '[{"x": 5}]')

    def test_tojsonstring_rect(self):
        """test to_json_string with rectangle subclass"""
        a = Rectangle(10, 5, 2, 2)
        dict = a.to_dictionary()
        json_string = Base.to_json_string([dict])
        dict = str([dict])
        dict = dict.replace("'", '"')
        self.assertEqual(dict, json_string)

    def test_tojsonstring_square(self):
        """test to_json_string with square subclass"""
        a = Square(5, 2, 2)
        dict = a.to_dictionary()
        json_string = Base.to_json_string([dict])
        dict = str([dict])
        dict = dict.replace("'", '"')
        self.assertEqual(dict, json_string)

    def test_savetofile_emptyrect1(self):
        """test save_to_file class method no rectangle"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_savetofile_emptyrect2(self):
        """test save_to_file with empty rectangle"""
        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_savetofile_rectangle(self):
        """test save_to_file with rectangle"""
        a = Rectangle(1, 2)
        Rectangle.save_to_file([a])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 53)

    def test_savetofile_emptysquare1(self):
        """test save_to_file no square"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_savetofile_emptysquare2(self):
        """test save_to_file empty square"""
        os.remove("Rectangle.json")
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_savetofile_square(self):
        """test save_to_file with square"""
        a = Square(1)
        Square.save_to_file([a])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 39)

    def test_savetofile_multiple(self):
        """test save_to_file with multiple dictionaries"""
        a = Rectangle(10, 5, 1, 2)
        b = Rectangle(1, 2)
        Rectangle.save_to_file([a, b])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 107)

    def test_fromjsonstring_noargs(self):
        """test from_json_string static method with 0 arguments"""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        a = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(e.exception), a)

    def test_fromjsonstring_empty(self):
        """test from_json_string with empty string"""
        self.assertEqual(Base.from_json_string(""), [])

    def test_fromjsonstring_return(self):
        """test from_json_string returns dictionary of string"""
        a = '[{"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}]'
        b = [{'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5}]
        self.assertEqual(Base.from_json_string(a), b)

    def test_fromjsonstring_after_tojsonstring(self):
        """test from_json_string of output from to_json_string"""
        original = [{'id': 1, 'width': 2, 'height': 3}]
        converted = Rectangle.to_json_string(original)
        returned = Rectangle.from_json_string(converted)
        self.assertEqual(original, returned)

    def test_create(self):
        """test create class method"""
        old = Rectangle(3, 5, 1)
        old_dict = old.to_dictionary()
        new = Rectangle.create(**old_dict)
        self.assertEqual(str(old), str(new))
        self.assertFalse(old is new)
        self.assertFalse(old == new)

    def test_loadfromfile_rectangle(self):
        """test load_from_file class method rectangle"""
        a = Rectangle(10, 5, 1, 2)
        b = Rectangle(2, 4)
        original = [a, b]
        Rectangle.save_to_file(original)
        returned = Rectangle.load_from_file()
        self.assertNotEqual(id(original[0]), id(returned[0]))
        self.assertEqual(str(original[0]), str(returned[0]))
        self.assertNotEqual(id(original[1]), id(returned[1]))
        self.assertEqual(str(original[1]), str(returned[1]))

    def test_loadfromfile_square(self):
        """test load_from_file class method square"""
        a = Square(5)
        b = Square(5, 1, 2)
        original = [a, b]
        Square.save_to_file(original)
        returned = Square.load_from_file()
        self.assertNotEqual(id(original[0]), id(returned[0]))
        self.assertEqual(str(original[0]), str(returned[0]))
        self.assertNotEqual(id(original[1]), id(returned[1]))
        self.assertEqual(str(original[1]), str(returned[1]))

if __name__ == "__main__":
    unittest.main()
