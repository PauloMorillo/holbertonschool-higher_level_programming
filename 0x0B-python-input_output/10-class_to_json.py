#!/usr/bin/python3
def class_to_json(obj):
    """Function to returns dictionary description with simple data struct"""
    return obj.__dict__
