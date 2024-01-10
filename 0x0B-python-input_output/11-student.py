#!/usr/bin/python3
"""student class"""


class Student:
    """a student"""

    def __init__(self, first_name, last_name, age):
        """new Student-> Args: first_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return student as dictionary"""
        try:
            for a in attrs:
                if type(a) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dic = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dic[key] = value
        return new_dic

    def reload_from_json(self, json):
        """replace attributes of student"""
        for key, value in json.items():
            self.__dict__[key] = value
