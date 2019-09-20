#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    return list(map(lambda x: my_list[x] * number, range(len(my_list))))
