#!/usr/bin/python3
'''
read file
'''
import json


def load_from_json_file(filename):
    '''function to read file'''
    with open(filename, "r", encoding='utf-8') as File:
        x = json.load(File)
        return(x)
