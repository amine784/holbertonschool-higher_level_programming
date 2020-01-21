#!/usr/bin/python3
'''
return subclass or not
'''


class BaseGeometry:
    '''class BaseGeometry'''
    def area(self):
        '''method'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''integer validator'''
        x = type(value)
        if x is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
