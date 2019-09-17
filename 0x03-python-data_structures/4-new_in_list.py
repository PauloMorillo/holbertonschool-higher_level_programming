#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cmy_list = my_list[0:]
    if idx < len(cmy_list) and idx >= 0:
        cmy_list[idx] = element
        return cmy_list
    else:
        return cmy_list
