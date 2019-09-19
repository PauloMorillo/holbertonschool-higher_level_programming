#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    listn = list(a_dictionary.keys())
    a = 0
    newdic = a_dictionary.copy()
    while a < len(listn):
        newdic.update({listn[a]: a_dictionary.get(listn[a]) * 2})
        a = a + 1
    return newdic
