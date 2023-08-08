#!/usr/bin/python3
def funct():
    for i in reversed(range(65, 91)):
        if i % 2 == 0:
            i+=32
            print(chr(i), end="")
        else:
            print(chr(i), end="")
funct()
