def no_c(my_string):
    a = 0
    cmy_string = ""
    while a < len(my_string):
        if my_string[a] == 'c' or my_string[a] == 'C':
            a = a + 1
        cmy_string = cmy_string + my_string[a]
        a = a + 1
    return cmy_string
