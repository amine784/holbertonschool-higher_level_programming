#!/usr/bin/python3
'''
read file
'''


def number_of_lines(filename=""):
    '''function to read file'''
    with open(filename, "r", encoding='utf-8') as File:
        return(len(File.readlines()))
