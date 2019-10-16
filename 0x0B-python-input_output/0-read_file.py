def read_file(filename=""):
    """Function to read a file"""
    with open(filename, encoding="UTF-8") as f:
        data = f.read()
    f.close()
    print(data)
