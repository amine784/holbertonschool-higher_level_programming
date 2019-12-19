#!/usr/bin/python3
def search_replace(my_list, search, replace):
    search -= 1
    liste = []
    liste = my_list.copy()
    for i in liste:
        if i == search:
            liste[i] = replace
    return(liste)
