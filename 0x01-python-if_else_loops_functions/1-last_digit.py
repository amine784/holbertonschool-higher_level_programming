#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    l = number % 10
st = "and is less than 6 and not 0"
if number < 0:
    l = number % (10 * (-1))
if l == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, l))
elif l > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, l))
elif l < 6 and l != 0:
    print("Last digit of {:d} is {:d} {:s}".format(number, l, st))
