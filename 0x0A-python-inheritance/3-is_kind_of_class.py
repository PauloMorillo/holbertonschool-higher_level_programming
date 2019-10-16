#!/usr/bin/python3
""" module with function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
        """Function to know if an object is an instance or inherited a class"""
        return isinstance(obj, a_class)
