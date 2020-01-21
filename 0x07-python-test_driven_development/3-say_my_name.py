#!/usr/bin/python3
'''
functino that print name
say my
name
'''


def say_my_name(first_name, last_name=""):
    '''
    method to print name
    '''
    if type(first_name) is not str or len(first_name) == 0:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
