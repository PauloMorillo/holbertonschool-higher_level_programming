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

        def area(self):
                """Function to know area of rectangle"""
                return self.__width * self.__height

        def __str__(self):
                """Function to return a string"""
                return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
        """Class Square inherit from rectangle"""
        def __init__(self, size):
                """Function to aign size"""
                self.integer_validator("size", size)
                self.__size = size
                super().__init__(self.__size, self.__size)
