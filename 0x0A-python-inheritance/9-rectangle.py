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

    def area(self):
        '''def area'''
        return(self.__width * self.__height)

    def __str__(self):
        '''str method'''
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
