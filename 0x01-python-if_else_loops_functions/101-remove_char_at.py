#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    newstr = ""
    while count < len(str):
        if count == n:
            count = count + 1
        conca = str[count]
        newstr = newstr + conca
        count = count + 1
    return newstr
