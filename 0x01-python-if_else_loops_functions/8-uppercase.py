#!/usr/bin/python3
def uppercase(str):
    count = 0
    while count < len(str):
        chasc = ord(str[count])
        if chasc >= 97 and chasc <= 122:
            chasc = chr(chasc - 32)
        else:
            chasc = chr(chasc)
        print("{}".format(chasc), end="")
        count = count + 1
    print("")
