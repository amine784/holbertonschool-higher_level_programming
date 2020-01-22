#!/usr/bin/python3
'''
read file
'''


def write_file(filename="", text=""):
    '''function to read file'''
    with open(filename, "w", encoding='utf-8') as File:
        return(File.write(text))
