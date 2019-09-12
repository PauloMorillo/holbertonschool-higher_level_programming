#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    count = 0
    argc = len(argv)
    if argc > 1:
        if argc == 2:
            print("1 argument:")
        else:
            print(argc - 1, "arguments:")
        count = count + 1
        while count < argc:
            print("{:d}: {}".format(count, argv[count]))
            count = count + 1
    else:
        print(count, "arguments.")
