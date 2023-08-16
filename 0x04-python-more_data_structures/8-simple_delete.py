#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        if key is str:
            a_dictionary.pop(key)
        else:
            return None
    else:
        return None
    return a_dictionary
