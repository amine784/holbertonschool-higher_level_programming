#!/usr/bin/python3
def remove_char_at(str, n):
    strr = ""
    l = len(str)
    for a in range(l):
        if a != n:
            strr = strr + str[a]
    return(strr)
