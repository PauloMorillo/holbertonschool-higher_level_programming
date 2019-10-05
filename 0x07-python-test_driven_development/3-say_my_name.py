#!/usr/bin/python3
"""
Function to print square
"""


def say_my_name(first_name, last_name=""):
    """
    first_name input name
    last_name

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
