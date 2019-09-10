#!/usr/bin/python3
a = 0
b = 1
while a <= 9:
    while b <= 9:
        if a < b:
            if a == 8 and b == 9:
                break
            print("{:d}".format(a), end="")
            print("{:d}, ".format(b), end="")
        b = b + 1
    b = 0
    a = a + 1
print("{:d}".format(89))
