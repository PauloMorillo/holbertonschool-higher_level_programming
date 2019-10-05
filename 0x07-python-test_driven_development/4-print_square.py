#!/usr/bin/python3
"""
function to print square
"""


def print_square(size):
    """
    size is the size of square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    a = 0
    while a < size:
        print("#" * size)
        a = a + 1
