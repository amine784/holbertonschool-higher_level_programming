#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l = len(my_list)
    copy_list = my_list[:]
    if idx < 0 or idx >= l:
        return(copy_list)
    else:
        copy_list[idx] = element
        return(copy_list)
