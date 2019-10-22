#!/usr/bin/python3
"""Module with Square class"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Square class from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square begins here"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Function to Return string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    @property
    def size(self):
        """Getter value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """Function to update values of square"""
        atr = ["id", "size", "x", "y"]
        if not args:
            if kwargs:
                keys = list(kwargs)
                for i in range(len(keys)):
                    setattr(self, keys[i], kwargs[keys[i]])
        if len(atr) < len(args):
            leng = len(atr)
        else:
            leng = len(args)
        for i in range(leng):
            setattr(self, atr[i], args[i])

    def to_dictionary(self):
        """Function to return dictionary"""
        return {'id': self.id, 'x': self.x, 'size': self.__size,
                'y': self.y}
