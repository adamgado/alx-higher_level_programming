#!/usr/bin/python3
"""square class functions"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return str representation of square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        """size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign arguments if args or kwargs"""
        if args:
            self.__assign(*args)
        elif kwargs:
            self.__assign(**kwargs)

    def __assign(self, id=None, size=None, x=None, y=None):
        """internal function that assigns arguments to attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """return dictionary representation of square"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
