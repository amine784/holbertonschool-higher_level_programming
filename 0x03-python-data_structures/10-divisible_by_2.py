#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bl = []
    for i in range(len(my_list)):
        if int(my_list[i]) % 2 == 0:
            bl.append(True)
        else:
            bl.append(False)
    return(bl)
