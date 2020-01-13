#!/usr/bin/python3
'''
function  thats
split text
str
'''


def text_indentation(text=''):
    '''
    method
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = False
    for i in text:
        if x is False and i == ' ':
                continue
        x = True
        if i in "?:.":
            print("{}\n".format(i))
            x = False
        else:
            print("{}".format(i), end="")
