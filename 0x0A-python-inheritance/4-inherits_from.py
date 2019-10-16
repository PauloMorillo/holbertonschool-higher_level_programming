#!/usr/bin/python3
""" module with function inherits_from"""


def inherits_from(obj, a_class):
        """Function to know if an object is an instance from a subclass"""
        return (issubclass(obj.__class__, a_class) and type(obj) != a_class)
