#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = (my_list[::-1])
    l = len(my_list)
    for i in range(l):
        print("{:d}".format(my_list[i]))
