#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = number % 10
if number < 0:
    l = number * (-1) % 10
if l == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, l))
if l > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, l))
if l < 6 and l != 0:
    print("Last digit of {:d} is {:d} ".format(number, l), end='')
    print ("and is less than 6 and not 0")
