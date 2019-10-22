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
            t = []
            if list_objs is not None:
                i = 0
                while i < len(list_objs):
                    t.append(list_objs[i].to_dictionary())
                    i = i + 1
            f.write(cls.to_json_string(t))

    @staticmethod
    def from_json_string(json_string):
        """Function to change from json to lsit"""
        if json_string is None or json_string is []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Fucntion to returns an instance with all attributes already set"""
        du = cls(1, 1, 1, 1)
        du.update(**dictionary)
        return du

    @classmethod
    def load_from_file(cls):
        """Function to load a list of instances"""
        with open(cls.__name__ + ".json", 'r') as f:
            if not f:
                return []
            lisob = cls.from_json_string(f.read())
            lisnob = []
            for dic in range(len(lisob)):
                lisnob = lisnob + [cls.create(**lisob[0][dic])]
            return lisnob
