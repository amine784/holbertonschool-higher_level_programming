#!/usr/bin/python3
def uniq_add(my_list=[]):
    sett = set(my_list)
    s = 0
    l = len(sett)
    for i in sett:
        s += i
    return(s)
