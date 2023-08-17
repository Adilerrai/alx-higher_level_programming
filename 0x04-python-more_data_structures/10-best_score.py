#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif len(a_dictionary) == 0:
        return None
    else:
        best_score = max(a_dictionary)
    return best_score
