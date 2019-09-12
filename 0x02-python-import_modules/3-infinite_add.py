#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    count = 1
    argc = len(argv)
    suma = 0
    if argc > 1:
        while count < argc:
            suma = suma + int(argv[count])
            count = count + 1
    print("{:d}".format(suma))
