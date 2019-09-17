#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    a = 1
    maxi = my_list[0]
    while a < len(my_list):
        if my_list[a] > maxi:
            maxi = my_list[a]
        a = a + 1
    return maxi
