#!/usr/bin/python3
def common_elements(set_1, set_2):
    seta = list(set_1)
    setb = list(set_2)
    a = 0
    b = 0
    c = []
    while a < len(seta):
        while b < len(setb):
            if seta[a] == setb[b]:
                c = c + [seta[a]]
            b = b + 1
        b = 0
        a = a + 1
    return c
