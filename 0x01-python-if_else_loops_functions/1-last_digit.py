#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
if number < 0:
    lastd = -lastd
print(f"Last digit of {number:d} is {lastd:d} and is ", end="")
if lastd > 5:
    print("greater than 5")
elif lastd == 0:
    print("0")
else:
    print("less than 6 and not 0")
