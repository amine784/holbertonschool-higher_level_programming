#!/usr/bin/python3
def no_c(my_string):
    copy_st = ""
    for x in (my_string):
        if x == "c" or x == "C":
            continue
        copy_st += x
    return (copy_st)
