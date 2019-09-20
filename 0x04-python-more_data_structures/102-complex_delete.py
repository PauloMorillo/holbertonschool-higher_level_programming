#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        a = 0
        while a < len(keys):
            if value == a_dictionary.get(keys[a]):
                del a_dictionary[keys[a]]
            a = a + 1
        return a_dictionary
    return None
