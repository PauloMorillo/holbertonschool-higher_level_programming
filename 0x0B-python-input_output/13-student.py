#!/usr/bin/python3
"""Module with class"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """all begin here"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function to return dict of object"""
        if attrs is None:
            return self.__dict__
        if type(attrs) == list:
            keyss = self.__dict__
            a = 0
            realatt = dict()
            while a < len(attrs):
                if attrs[a] in keyss:
                    realatt[attrs[a]] = keyss[attrs[a]]
                a = a + 1
        return realatt

    def reload_from_json(self, json):
        """Funtion to set new attributes"""
        keys = list(json)
        a = 0
        while a < len(keys):
            setattr(self, keys[a], json[keys[a]])
            a = a + 1
