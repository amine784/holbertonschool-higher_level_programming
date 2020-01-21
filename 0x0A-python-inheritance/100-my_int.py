#!/usr/bin/python3
'''
return subclass or not
'''


class MyInt(int):
    '''class my int'''
    def __ne__(self, other):
        '''method spec not equal'''
        return(int(self) == int(other))

    def __eq__(self, other):
        '''method spec equal'''
        return(int(self) != int(other))
