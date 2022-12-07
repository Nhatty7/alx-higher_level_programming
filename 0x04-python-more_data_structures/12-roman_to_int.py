#!/usr/bin/python3
def roman_to_int(roman_string):
    # Fail checks, none, not a string
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    # Dictionary for roman numerals
    romanDiction = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    res = 0
    temp = list(roman_string)
    # Concat 4 and 9s
    if len(temp) > 1:
        k = 0
        for i in temp:
            try:
                if temp[k] == 'I' and temp[k + 1] == 'V':
                    temp[k:k + 2] = [''.join(temp[k:k + 2])]
            except IndexError:
                pass
            try:
                if temp[k] == 'I' and temp[k + 1] == 'X':
                    temp[k:k + 2] = [''.join(temp[k:k + 2])]
            except IndexError:
                pass
            k += 1
    # Search in dict for correct numbers and add
    for k, v in romanDiction.items():
        for index in temp:
            if index == k:
                res += v
    return res
