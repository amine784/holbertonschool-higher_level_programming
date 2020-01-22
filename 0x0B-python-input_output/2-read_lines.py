#!/usr/bin/python3
'''
read file
'''


def read_lines(filename="", nb_lines=0):
    '''function to read file'''
    with open(filename, "r", encoding='utf-8') as File:
        if nb_lines == 0 or nb_lines < 0:
            print(File.read(), end="")
        for line in range(nb_lines):
            print(File.readline(), end="")
