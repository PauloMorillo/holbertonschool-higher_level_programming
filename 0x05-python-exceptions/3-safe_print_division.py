#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        an = a / b
    except:
        an = "None"
        return None
    finally:
        print("Inside result:", an)
    return an
