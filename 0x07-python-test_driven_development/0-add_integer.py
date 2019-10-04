#!/usr/bin/python3
def add_integer(a, b=98):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    if type(a) == int:
        pass
    elif type(a) == float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) == int:
        pass
    elif type(b) == float:
        b = int(b)
    else:
                raise TypeError("b must be an integer")
    return a + b
