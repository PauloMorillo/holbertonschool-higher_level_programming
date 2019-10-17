#!/usr/bin/python3
if __name__ == "__main__":
    load_from_json_file = __import__('8-load_from'
                                     '_json_file').load_from_json_file
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

    import sys
    try:
        fli = load_from_json_file('add_item.json')
    except:
        fli = []
    argv = sys.argv
    count = 1
    argc = len(argv)
    if argc > 1:
        while count < argc:
            fli.append(argv[count])
            count = count + 1
    save_to_json_file(fli, 'add_item.json')
