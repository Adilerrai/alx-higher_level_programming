#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        temp = -(-1*int(abs(number) % 10))
        return temp
    else:
        temp = number % 10
        return temp
