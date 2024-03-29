#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        if op == '+':
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif op == 'x':
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif op == "/":
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
        elif op == "-":
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
