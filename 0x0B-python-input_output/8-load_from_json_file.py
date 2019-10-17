#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Function fomr obj to JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
