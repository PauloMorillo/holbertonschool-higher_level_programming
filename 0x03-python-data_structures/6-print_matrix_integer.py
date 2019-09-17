#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        a = 0
        b = 0
        if matrix:
                while a < len(matrix):
                        b = 0
                        while b < len(matrix[0]):
                                print("{:d}".format(matrix[a][b]), end="")
                                b = b + 1
                                if b != len(matrix[0]):
                                        print(" ", end="")
                        print("")
                        a = a + 1
        else:
                print("")
