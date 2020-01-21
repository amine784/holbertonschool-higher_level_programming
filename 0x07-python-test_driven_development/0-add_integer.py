#!/usr/bin/python3
'''
function that
add 2 int
deff
'''


def add_integer(a, b=98):
    '''
    function that add 2 integer
    '''
    messageErrorA = "a must be an integer"
    messageErrorB = "b must be an integer"
    x = type(a)
    y = type(b)
    if x is not int and x is not float:
        raise TypeError(messageErrorA)
    if y is not int and y is not float:
        raise TypeError(messageErrorB)
    x = a + b
    if x < 0:
        x = x * -1
    if x == float("inf"):
        raise ValueError("overflow")
    else:
        return(int(a) + int(b))
