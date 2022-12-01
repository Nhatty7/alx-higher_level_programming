#!/usr/bin/python3

for alf in range(ord('a'), ord('z') + 1):
    if chr(alf) != 'e' and alf != 'q':
        print("{:c}".format(alf), end="")
