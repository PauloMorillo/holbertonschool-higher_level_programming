#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        if roman_string.isalpha():
            nrom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                    "M": 1000}
            a = 1
            if roman_string[a - 1] in nrom:
                intro = [nrom[roman_string[a - 1]]]
            else:
                return 0
            maxi = 0
            while a < len(roman_string):
                b = roman_string[a]
                if b in nrom:
                    intro = intro + [nrom[b]]
                else:
                    return 0
                if nrom[b] > nrom[roman_string[a - 1]]:
                    maxi = 1
                a = a + 1
            if maxi == 1:
                return sum(intro) - 2
            else:
                return sum(intro)
        else:
            return 0
    else:
        return 0
