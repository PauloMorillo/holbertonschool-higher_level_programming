#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        while a < x:
            print(my_list[a], end="")
            a = a + 1
    except:
        print("")
        return a
    print("")
    return a
