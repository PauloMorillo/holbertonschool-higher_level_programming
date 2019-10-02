#!/usr/bin/python3
"""The __init__ method may be documented in either the class level
docstring, or as a docstring on the __init__ method itself."""


class Square:
    def __init__(self, size=0):
        try:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise Exception("size must be an integer")
