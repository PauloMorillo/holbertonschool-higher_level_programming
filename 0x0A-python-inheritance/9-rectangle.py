#!/usr/bin/python3
""" module with function inherits_from"""


class BaseGeometry:
        """Class BaseGeometry"""
        def area(self):
                """Function to raise an error"""
                raise Exception("area() is not implemented")

        def integer_validator(self, name, value):
                """Function to validates value"""
                if type(value) != int:
                        raise TypeError("{} must be an integer".format(name))
                if value <= 0:
                        raise ValueError("{} must be greater "
                                         "than 0".format(name))


class Rectangle(BaseGeometry):
        """Class Rectangle that inherits from BaseGeometry"""
        def __init__(self, width, height):
                """Function init all begins here"""
                super().integer_validator("width", width)
                self.__width = width
                super().integer_validator("height", height)
                self.__height = height
