#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = 0
    an = []
    while a < list_length:
        try:
            divi = my_list_1[a] / my_list_2[a]
            a = a + 1
        except TypeError:
            divi = 0
            a = a + 1
            print("wrong type")
        except ZeroDivisionError:
            divi = 0
            print("division by 0")
            a = a + 1
        except:
            divi = 0
            a = a + 1
            print("out of range")
        finally:
            an = an + [divi]
    return an
