#!/usr/bin/python3
""" This module is a search for a peak in a list"""


def find_peak(list_of_integers):
    """this function return the peak of a lsit"""
    if len(list_of_integers) > 0:
        return max(list_of_integers)
    return None
