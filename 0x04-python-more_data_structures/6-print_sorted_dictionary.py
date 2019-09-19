#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listn = list(sorted(a_dictionary.keys()))
    a = 0
    while a < len(listn):
        print("{}: {}".format(listn[a], a_dictionary.get(listn[a])))
        a = a + 1
