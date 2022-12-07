#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a = 0
    best = ''
    for i, j in a_dictionary.items():
        if j > a:
            a = j
            best = i
    return best
