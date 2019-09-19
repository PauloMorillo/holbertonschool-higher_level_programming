#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = 0
    b = 0
    c = []
    d = []
    while a < len(matrix):
        while b < len(matrix[0]):
            c = c + [matrix[a][b] ** 2]
            b = b + 1
        b = 0
        d = d + [c]
        c = []
        a = a + 1
    return d
