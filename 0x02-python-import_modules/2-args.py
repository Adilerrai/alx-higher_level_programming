#!/usr/bin/python3
from sys import argv


def argv_list(n):
    for i in range(1, n+1):
        print("{}: {}".format(i, argv[i]))


def argument_number(n):
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 arguments.")
    else:
        print("{} arguments.".format(len(argv)-1))


if __name__ == "__main__":
    n = len(argv) -1
             
    argument_number(n)
    argv_list(n)

