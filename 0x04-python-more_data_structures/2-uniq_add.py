#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = my_list.copy()
    new.sort()
    a = 0
    while a < len(new):
        b = a + 1
        while b < len(new):
            if new[a] == new[b] and new[b] != 0:
                new[b] = 0
            b = b + 1
        a = a + 1
    return sum(new)
