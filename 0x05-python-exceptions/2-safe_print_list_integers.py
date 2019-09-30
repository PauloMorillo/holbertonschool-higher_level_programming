#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    while a < x:
        try:
            print("{:d}".format(my_list[a]), end="")
            a = a + 1
        except TypeError:
            a = a + 1
        except ValueError:
            a = a + 1
    print("")
    return a
