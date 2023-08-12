#!/usr/bin/python3


def tuple_to_list(tuple_i):
    temp_list = list(tuple_i)
    n = len(temp_list)

    while n < 2:
        temp_list.append(0)
        n += 1
    return temp_list

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_to_list(tuple_a)
    b = tuple_to_list(tuple_b)
    c = []
    for i in range(2):
        c.append(a[i] + b[i])
    return tuple(c)
