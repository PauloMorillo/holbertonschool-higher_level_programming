#!/usr/bin/python3
def number_of_lines(filename=""):
    """Function to return number of lines"""
    with open(filename, 'r') as f:
        lines = 0
        while f.readline():
            lines = lines + 1
        return lines
    f.close()
