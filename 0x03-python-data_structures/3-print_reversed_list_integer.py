#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = 0
    my_list.reverse()
    while a < len(my_list):
        print("{:d}".format(my_list[a]))
        a = a + 1
    my_list.reverse()
