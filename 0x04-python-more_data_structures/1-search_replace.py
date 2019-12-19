#!/usr/bin/python3
def search_replace(my_list, search, replace):
    liste = []
    l = len(my_list)
    for i in range(l):
        if my_list[i] != search:
            liste.append(my_list[i])
        else:
            liste.append(replace)
    return(liste)
