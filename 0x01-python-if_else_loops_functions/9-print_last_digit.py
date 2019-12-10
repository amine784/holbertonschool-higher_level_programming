#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        l = 0
        print("{:d}".format(l), end="")
        return(l)
    if number < 0:
        l = number % (10 * (-1))
        print("{:d}".format(l * (-1)), end="")
        return(l * (-1))
    if number > 0:
        l = number % 10
        print("{:d}".format(l), end="")
        return(l)
