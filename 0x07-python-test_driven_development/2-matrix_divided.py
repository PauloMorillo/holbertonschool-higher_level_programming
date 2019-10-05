#!/usr/bin/python3
"""
This is the module to divide a matrix by any number int or float.
"""


def matrix_divided(matrix, div):
    """Matrix divided function

    Args:
         matrix: first input matrix to divide
         div: int or float to divide

    Returns:
          The return value is new atrix divided by div
    """
    if type(div) == int or type(div) == float:
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
    if type(matrix) == list and type(matrix[0]) == list:
        if len(matrix[0]) < 1:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        newma = [matrix[0][:] for i in matrix]
        lenr = len(matrix[0])
        a = 0
        while a < len(matrix):
            b = 0
            while b < len(matrix[a]):

                if type(matrix[a][b]) != int and type(matrix[a][b]) != float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                newma[a][b] = round((matrix[a][b] / div), 2)
                b = b + 1
            if a < len(matrix[a]) - 1:
                if lenr != len(matrix[a + 1]):
                    raise TypeError("Each row of the matrix must have the same size")
            a = a + 1
        return newma
    else:
         raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
