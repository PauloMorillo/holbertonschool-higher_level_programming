#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        a = 1
        maxin = a_dictionary.get(keys[0])
        maxik = keys[0]
        while a < len(keys):
            if maxin < a_dictionary.get(keys[a]):
                maxik = keys[a]
                maxin = a_dictionary.get(keys[a])
            a = a + 1
        return maxik
    return None
