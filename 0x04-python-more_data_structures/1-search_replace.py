#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = map(lambda a: replace if a - search == 0 else a, my_list)
    return list(new_list)
