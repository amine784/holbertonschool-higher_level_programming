#!/usr/bin/python3
'''
return subclass or not
'''


def inherits_from(obj, a_class):
    '''isinstance class'''
    typ = type(obj)
    if typ is a_class:
        return(False)
    else:
        return(isinstance(obj, a_class))
