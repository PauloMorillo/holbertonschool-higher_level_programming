#!/usr/bin/python3
a = 00
while a <= 99:
    if a < 99:
        print("{:02d}, ".format(a, a), end="")
    else:
        print("{:d}".format(a))
    a = a + 1
