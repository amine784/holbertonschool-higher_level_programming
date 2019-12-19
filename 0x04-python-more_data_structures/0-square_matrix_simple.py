#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtrice = []
    for i in matrix:
        mtrice.append([j ** 2 for j in i])
    return(mtrice)
