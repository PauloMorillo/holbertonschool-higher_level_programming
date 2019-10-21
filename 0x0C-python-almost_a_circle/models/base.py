#!/usr/bin/python3
"""Module with base"""


class Base:
    """Class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init to begin class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
