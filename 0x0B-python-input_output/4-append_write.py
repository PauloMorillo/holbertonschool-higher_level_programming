#!/usr/bin/python3
def append_write(filename="", text=""):
    """Function to write a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
    f.close()
