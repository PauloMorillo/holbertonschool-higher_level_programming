#!/usr/bin/python3
"""Module with class"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """all begin here"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function to return dict of object"""
        return self.__dict__
