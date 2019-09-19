#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = 0
    b = my_list.copy()
    while a < len(my_list):
        if my_list[a] == search:
            b[a] = replace
        a = a + 1
    return b
