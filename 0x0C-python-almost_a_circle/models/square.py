#!/usr/bin/python3
'''new class square'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''new class that inherite from Base'''
    def __init__(self, size, x=0, y=0, id=None):
        '''new methode'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str def'''
        return("[Square] ({}) {}/{} - {}"
               .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        '''self size'''
        return(self.width)

    @size.setter
    def size(self, value):
        ''' size'''
        self.width = value
        self.height = value

    def to_dictionary(self):
        '''convert to dictionary'''
        return({"id": self.id, "size": self.size,
                "x": self.x, "y": self.y})
