#!/usr/bin/python3
class Square:
    ''' define a neww class called square '''
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''class method that calculate the area of square'''
        return (self.__size * self.__size)
