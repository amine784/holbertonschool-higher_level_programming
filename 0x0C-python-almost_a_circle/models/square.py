#!/usr/bin/python3
'''new class square'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''new class that inherite from Base'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return("[Square] ({:d}) {:d}/{:d} - {:d}".
               format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return(self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update att and key'''
        if(args is not None) and (len(args) > 0):
            for i in range(0, len(args)):
                for arg in args:
                    if j == 0:
                        self.id = arg
                    elif j == 1:
                        self.size = arg
                    elif j == 2:
                        self.x = arg
                    elif j == 3:
                        self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''convert to dictionary'''
        return({"id": self.id, "size": self.size,
                "x": self.x, "y": self.y})
