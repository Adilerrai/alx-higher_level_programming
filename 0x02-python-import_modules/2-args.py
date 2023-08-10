#!/usr/bin/python3
import sys
if __name__ == "__main__é=":
    n = len(sys.argv) - 1
    print("{} arguments:".format(n))
    for i in range(1, n+1):
        print("{}: {}".format(i, sys.argv[i]))
