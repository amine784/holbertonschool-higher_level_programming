#!/usr/bin/python3
'''
read file
'''


def read_file(filename=""):
    '''function to read file'''
    with open(filename, "r", encoding='utf-8') as File:
        content = File.read()
        print(content, end="")
