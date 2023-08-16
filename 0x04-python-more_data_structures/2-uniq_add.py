#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    temp_set = set(my_list)
    temp_list = list(temp_set)
    for i in range(0, len(temp_list)-1):
        sum += temp_list[i]
        return sum
