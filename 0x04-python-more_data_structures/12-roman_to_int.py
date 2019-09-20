#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        if roman_string.isalpha():
            roman = roman_string
            if "VV" in roman or "LL" in roman or "DD" in roman:
                return 0
            if (
                    "IL" in roman or "IC" in roman or "ID" in roman or "IM"
                    in roman):
                return 0
            if "XD" in roman or "XM" in roman:
                return 0
            if (
                    "IIII" in roman or "XXXX" in roman or "CCCC" in roman or
                    "MMMM" in roman):
                return 0
            nrom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                    "M": 1000}
            a = 1
            rep = 0
            if roman[a - 1] in nrom:
                intro = [nrom[roman[a - 1]]]
            else:
                return 0
            maxi = 0
            while a < len(roman):
                b = roman[a]
                if b in nrom:
                    intro = intro + [nrom[b]]
                else:
                    return 0
                if nrom[b] > nrom[roman[a - 1]]:
                    maxi = maxi + 1
                    subst = nrom[roman[a - 1]]
                    rep = 0
                if nrom[b] <= nrom[roman[a - 1]] and maxi == 1:
                    return 0
                a = a + 1
            if maxi == 1:
                return sum(intro) - (subst * 2)
            elif maxi == 0:
                return sum(intro)
            else:
                return 0
        else:
            return 0
    else:
        return 0
