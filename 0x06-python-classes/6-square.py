#!/usr/bin/python3
"""The __init__ method may be documented in either the class level
docstring, or as a docstring on the __init__ method itself."""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
            type(value[0]) != int or value[0] < 0 or
                type(value[1]) != int or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            a = 0
            while a < self.__size:
                b = 0
                c = 0
                d = 0
                while c < self.__position[0]:
                    if a == 0:
                        while d < self.__position[1]:
                            print()
                            d = d + 1
                    print("{}".format(" "), end="")
                    c = c + 1
                while b < self.__size:
                    print("{}".format("#"), end="")
                    b = b + 1
                print()
                a = a + 1
