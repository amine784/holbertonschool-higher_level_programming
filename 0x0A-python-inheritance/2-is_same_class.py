#!/usr/bin/python3
'''
return subclass or not
'''


def is_same_class(obj, a_class):
    '''sub class'''
    typ = type(obj)
    return(issubclass(a_class, typ))
