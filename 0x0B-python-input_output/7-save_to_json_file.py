#!/usr/bin/python3
'''
read file
'''
import json


def save_to_json_file(my_obj, filename):
    '''function to read file'''
    with open(filename, "w", encoding='utf-8') as File:
        x = json.dumps(my_obj)
        File.write(x)
