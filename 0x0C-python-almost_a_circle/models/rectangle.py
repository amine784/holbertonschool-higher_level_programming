#!/usr/bin/python3
'''new class rectangle'''

from models.base import Base


class Rectangle(Base):
    '''new class that inherite from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''funct to init class'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width'''
        return(self.__width)

    @width.setter
    def width(self, value):
        '''width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''heigth'''
        return(self.__height)

    @height.setter
    def height(self, value):
        '''height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''x'''
        return(self.__x)

    @x.setter
    def x(self, value):
        '''x get'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''y'''
        return(self.__y)

    @y.setter
    def y(self, value):
        ''' self y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''how to get the area surf'''
        return(self.__width * self.__height)

    def __str__(self):
        '''str rep'''
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        '''array'''
        rect = ""
        for i in range(self.y):
            print("")
        for j in range(self.height):
            rect = ' ' * self.x + '#' * self.width
            print(rect)

    def update(self, *args, **kwargs):
        '''update att and key'''
        if(args is not None) and (len(args) > 0):
            for i in range(0, len(args)):
                for arg in args:
                    if j == 0:
                        self.id = arg
                    elif j == 1:
                        self.width = arg
                    elif j == 2:
                        self.height = arg
                    elif j == 3:
                        self.x = arg
                    elif j == 4:
                        self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''convert to dictionary'''
        return({"id": self.id, "width": self.__width,
                "height": self.__height,
                "x": self.__x, "y": self.__y})
