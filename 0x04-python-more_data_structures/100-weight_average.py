#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return(0)
    tab = []
    for i in my_list:
        tab.append(i)
    sub = 0
    mul = 0
    somme = 0.0
    l = len(tab)
    for i in range(0, l):
        sub += tab[i][1]
        mul = tab[i][1] * tab[i][0]
        somme += mul
    somme /= sub
    return(somme)
