#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    l = len(matrix)
    while i < l:
        j = 0
        while j < len(matrix[i]):
            if j == 2:
                print ("{:d}".format(matrix[i][j]))
            else:
                print ("{:d} ".format(matrix[i][j]), end="")
            j = j + 1
        i = i + 1
        
