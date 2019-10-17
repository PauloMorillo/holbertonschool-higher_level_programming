#!/usr/bin/python3
def write_file(filename="", text=""):
    """Function to write a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
    f.close()
