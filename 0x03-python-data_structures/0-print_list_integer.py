#!/usr/bin/python3
def print_list_integer(my_list=[]):
    a = 0
    while a < len(my_list):
        print("{:d}".format(my_list[a]))
        a = a + 1
