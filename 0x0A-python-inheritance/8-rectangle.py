#!/usr/bin/python3
'''
return subclass or not
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class BaseGeometry'''
    def __init__(self, width, height):
        '''init conctructer'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
