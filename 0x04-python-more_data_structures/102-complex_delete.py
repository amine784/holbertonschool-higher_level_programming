#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in list(a_dictionary.keys()):
        if a_dictionary.keys() == value:
            a_dictionary.pop(key, 0)
    return(a_dictionary)
