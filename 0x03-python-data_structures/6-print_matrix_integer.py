#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        l = len(a)
        for b in range(0, l):
            l = len(a)
            if b == l - 1:
                print("{:d}".format(a[b]), end="")
            else:
                print("{:d}".format(a[b]), end=" ")
        print("")
