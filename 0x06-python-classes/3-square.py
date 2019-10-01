#!/usr/bin/pyhton3
class Square:
    def __init__(self, size=0):
        try:
            if size >= 0:
                self.__size = size
            else:
                raise Exception("size must be >= 0")
        except TypeError:
            raise Exception("size must be an integer")

    def area(self):
        return self.__size * self.__size
