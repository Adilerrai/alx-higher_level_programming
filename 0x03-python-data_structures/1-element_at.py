#!/usr/bin/python3


def element_at(my_list, idx):
    for i in range(0, len(my_list)):
        if idx == i:
            elem = my_list[i]
            return elem
