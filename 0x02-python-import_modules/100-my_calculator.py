#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    arglen = len(argv) - 1
    if arglen == 0:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    op = argv[2]
    a, b = int(argv[1]), int(argv[3])
    if op == "+":
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif op == "-":
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif op == "*":
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif op == "/":
        print('{} / {} = {}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
