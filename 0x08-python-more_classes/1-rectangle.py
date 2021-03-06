#!/usr/bin/python3
""" Rectangle class"""


class Rectangle:
    """ This is a Rectangle class"""
    def __init__(self, width=0, height=0):
        """Init method all begins here"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
