#!/usr/bin/python3
import json


def class_to_json(obj):
    """Function to returns dictionary description with simple data struct"""
    return json.dumps(obj.__dict__)
