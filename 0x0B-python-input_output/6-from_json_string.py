#!/usr/bin/python3
'''
read file
'''
import json


def from_json_string(my_str):
    '''function to read file'''
    return(json.loads(my_str))
