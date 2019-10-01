#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        an = fct(*args)
    except Exception as msg:
        sys.stderr.write("Exception: {}\n".format(msg))
        return None
    return an
