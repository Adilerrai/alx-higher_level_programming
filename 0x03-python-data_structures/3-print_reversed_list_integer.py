#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    if my_list is not None:
        temp_list= my_list[n-1::-1]
        for elem in temp_list:
            print("{:d}".format(elem))

