#!/usr/bin/python3
'''
return subclass or not
'''


def add_attribute(Objcet, Id, val):
    if hasattr(Objcet, "__dict__"):
        setattr(Objcet, Id, val)
    else:
        raise TypeError("can't add new attribute")
