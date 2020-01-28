#!/usr/bin/python3
'''
create base class
'''
import json


class Base:
    '''create new classe named base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''method of class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
