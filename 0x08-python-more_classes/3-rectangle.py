#!/usr/bin/python3
'''
function to set rectngle
widh
height
'''


class Rectangle:
    '''
    def method
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return(0)
        else:
            return((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        space = ""
        if self.__width == 0 or self.__height == 0:
            return(space)
        else:
            line = self.height
            for i in (0, line):
                for j in range(0, line):
                    x = '#' * self.width
                    print(x)
                return (x)
