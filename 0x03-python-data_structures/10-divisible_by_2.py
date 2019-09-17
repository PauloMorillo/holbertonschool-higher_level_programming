#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        a = 0
        t = []
        if my_list:
                while a < len(my_list):
                        if a % 2 == 0:
                                t.append(True)
                        else:
                                t.append(False)
                        a = a + 1
                return t
        else:
                return False
