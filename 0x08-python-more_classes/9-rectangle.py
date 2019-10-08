#!/usr/bin/python3
""" Rectangle class"""


class Rectangle:
    """ This is a Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init method all begins here"""
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """set height value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area method to calculate rectangule area"""
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter method to calculate rectangule perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Return rectangle like string"""
        strt = ""
        if self.__width == 0 or self.__height == 0:
            return strt
        for a in range(self.__height):
            for i in range(self.__width):
                strt = strt + str(self.print_symbol)
            strt = strt + "\n"
        return strt[:-1]

    def __repr__(self):
        """Return rectangle representation like Rectangle(w, h)"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Del an object"""
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """convert to square"""
        cls.__width = size
        cls.__height = size
        return Rectangle(size, size)
