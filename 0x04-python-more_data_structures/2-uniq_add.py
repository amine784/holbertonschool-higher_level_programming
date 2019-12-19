#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    l = len(my_list)
    for i in my_list:
        if type(i) == int:
            s += i
    return(s)
