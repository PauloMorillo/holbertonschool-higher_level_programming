#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Function to read a file"""
    with open(filename, encoding="UTF-8") as f:
        lines = 0
        while True:
            lines = lines + 1
            line = f.readline()
            print(line, end="")
            if lines == nb_lines:
                break
            if not line:
                break
    f.close()
