#!/usr/bin/python3
'''
read file
'''


def append_write(filename="", text=""):
    '''function to read file'''
    with open(filename, "a", encoding='utf-8') as File:
        return(File.write(text))
