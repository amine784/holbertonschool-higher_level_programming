#!/usr/bin/python3
'''
class base
'''
import json


class Base:
    '''base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''method of class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''share data with json format'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return("[]")
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        '''save to file'''
        if list_objs:
            liste = []
            liste.append([cls.to_dictionary(arg)for arg in list_objs])
        with open(cls.__name__ + ".json",
                  "w", encoding='utf-8') as File:
            File.write(cls.to_json_string(liste))
