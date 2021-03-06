#!/usr/bin/python3
"""
indent string
"""


def text_indentation(text):
    """
    text is the text to indent
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    a = 0
    p = a
    while a < len(text):
        if text[a] == '.' or text[a] == '?' or text[a] == ':':
            if a != p:
                if text[a + 1] == " ":
                    print(text[p:a + 1])
                    while text[a] == " ":
                        a = a + 1
                    p = a + 2
                else:
                    print(text[p:a + 1])
                    p = a + 1
                print()
        a = a + 1
    if p != a - 1:
        while text[p] == " ":
            p = p + 1
        print(text[p:], end="")
