#!/usr/bin/python3
a = 'a'
while a <= 'z':
    print("{}".format(a), end="")
    a = chr(ord(a) + 1)
