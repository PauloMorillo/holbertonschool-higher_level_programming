#!/usr/bin/python3
"""The __init__ method may be documented in either the class level
docstring, or as a docstring on the __init__ method itself."""


class Square:
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
