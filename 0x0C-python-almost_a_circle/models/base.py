#!/usr/bin/python3
"""Module with base"""

import json


class Base:
    """Class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init to begin class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function from dictionari to json"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function to save list in a file"""
        with open(cls.__name__ + ".json", 'w') as f:
            if not list_objs:
                f.write("[]")
            else:
                te = ""
                i = 0
                while i < len(list_objs):
                    te = te + cls.to_json_string(list_objs[i].to_dictionary())
                    i = i + 1
                f.write(te)

    @staticmethod
    def from_json_string(json_string):
        """Function to change from json to lsit"""
        if json_string is None or len(json_string) == 0:
            return []
        return [json.loads(json_string)]

    @classmethod
    def create(cls, **dictionary):
        """Fucntion to returns an instance with all attributes already set"""
        pass
