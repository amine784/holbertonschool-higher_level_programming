#!/usr/bin/python3
'''
function thats
print size in
dif ways
'''


def print_square(size):
    '''
    methodd
    '''
    messageError = "size must be an integer"
    messageErrorA = "size must be >= 0"
    spec = '#'
    if type(size)is not int:
        raise TypeError(messageError)
    if size < 0:
        raise ValueError(messageErrorA)
    if type(size)is float and size < 0:
        raise TypeError(messageError)
    for i in range(size):
        print(spec * size)
