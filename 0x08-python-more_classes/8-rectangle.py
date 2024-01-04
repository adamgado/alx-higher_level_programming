#!/usr/bin/python3
"""define 'rectangle' class"""


class Rectangle:
    """rectangle class

    Attributes:
        number_of_instances: rectangle instances count
        print_symbol: symbol for printing shape
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """return string to print Rectangle with #s"""
        shape = ""
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape += "\n".join(str(self.print_symbol) * self.__width
                           for a in range(self.__height))
        return shape

    def __repr__(self):
        """return string representation of rectangle to recreate"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print message on rectangle delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return rectangle with larger area

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError: rect_1 or rect_2 not rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() <= rect_2.area():
            return (rect_2)
        return (rect_1)
