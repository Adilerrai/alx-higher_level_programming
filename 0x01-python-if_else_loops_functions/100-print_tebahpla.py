#!/usr/bin/python3
def funct():
    for i in reversed(range(65, 91)):
        if i % 2 == 0:
            i += 32
            output = chr(i)
        else:
            output = chr(i)
        print("{}".format(output), end="")


funct()
