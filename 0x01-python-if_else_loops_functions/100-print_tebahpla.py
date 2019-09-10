#!/usr/bin/python3
a = 'z'
ascv = ord(a)
count = 1
while a >= 'a':
    ascv = ord(a)
    if ((count % 2) == 0):
        ascv = chr(ascv - 32)
    else:
        ascv = chr(ascv)
    print("{}".format(ascv), end="")
    a = chr(ord(a) - 1)
    count = count + 1
