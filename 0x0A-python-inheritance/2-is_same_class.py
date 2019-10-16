#!/usr/bin/python3
""" module with function is_same_class"""


def is_same_class(obj, a_class):
        """Function to know if an object is from a class"""
        return (obj.__class__ == a_class)
