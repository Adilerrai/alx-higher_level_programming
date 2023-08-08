#!/usr/bin/python3
def print_last_digit(number):
    temp = abs(number) % 10
    print(temp, end="")
    return temp
