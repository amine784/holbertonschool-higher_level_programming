#!/usr/bin/python3
'''
read file
'''


def append_after(filename="", search_string="", new_string=""):
    '''def append after'''
    with open(filename, "r", encoding='utf-8') as File:
        line = File.readlines()
