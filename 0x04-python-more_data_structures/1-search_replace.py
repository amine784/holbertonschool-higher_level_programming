#!/usr/bin/python3
def search_replace(my_list, search, replace):
    liste = []
    for i in my_list:
        if i != search:
            liste.append(i)
        else:
            liste.append(replace)
    return(liste)
