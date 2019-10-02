#!/usr/bin/python3
"""The __init__ method may be documented in either the class level
docstring, or as a docstring on the __init__ method itself."""


class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    def __lt__(self, other):
        return(self.area() < other.area())

    def __le__(self, other):
        return(self.area() <= other.area())

    def __eq__(self, other):
        return(self.area() == other.area())

    def __ne__(self, other):
        return(self.area() != other.area())

    def __gt__(self, other):
        return(self.area() > other.area())

    def __ge__(self, other):
        return(self.area() >= other.area())
