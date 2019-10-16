#!/usr/bin/python3
def number_of_lines(filename=""):
    """Function to return number of lines"""
    with open(filename, 'r') as f:
        data = f.readline()
        lines = 1
        for line in f:
            lines = lines + 1
        return lines
    f.close()
