#!/usr/bin/python3
""" MyList class"""


class MyList(list):
    """ class with inheritance from list"""
    def print_sorted(self):
        """Method to print sorted list"""
        print(sorted(self))
