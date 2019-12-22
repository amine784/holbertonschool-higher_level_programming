#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return(None)
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    liste = []
    for r in roman_string:
        for i in roman:
            if r == i:
                x = roman.get(i)
                liste.append(x)
    l = (len(liste))
    s = 0
    for i in range(len(liste) - 1):
        if liste[i] < liste[i+1]:
            liste[i] = liste[i + 1] - liste[i]
            liste[i+1] = 0
    for i in range(len(liste)-1):
        if liste[i] < liste[i + 1]:
            liste[i] = liste[i + 1] - liste[i]
            liste[i + 1] = 0
    for st in liste:
        s = s + st
    return(s)
