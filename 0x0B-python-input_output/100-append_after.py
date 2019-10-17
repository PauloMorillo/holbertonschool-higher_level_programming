#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """Function to write a file"""
    with open(filename, 'r+') as f:
        data = f.read()
        pos = data.find(search_string)
        if pos >= 0:
            f.seek(pos, 0)
            return f.append(text)
    f.close()
