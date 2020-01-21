#!/usr/bin/python3
'''
function that devide
matrix per an int
equal
'''


def matrix_divided(matrix, div):
    '''
    metho that devide matrix per int or float
    '''
    messageError = "matrix must be a matrix (list of lists) of integers/floats"
    messageErrorB = "Each row of the matrix must have the same size"
    messageErrorC = "div must be a number"
    liste = []
    if type(matrix) is not list:
        raise TypeError(messageError)
    for i in matrix:
        if type(i) is not list:
            raise TypeError(messageError)
        if len(matrix[0]) != len(i):
            raise TypeError(messageErrorB)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(messageError)
    for m in matrix:
        new_liste = []
        if type(div) is not int and type(div) is not float:
            raise TypeError(messageErrorC)
        else:
            for k in m:
                new_liste.append(round((k / div), 2))
            liste.append(new_liste)
    return(liste)
