def matrix_divided(matrix, div):
    messageError = "matrix must be a matrix (list of lists) of integers/floats"
    messageErrorB = "Each row of the matrix must have the same size"
    messageErrorC = "div must be a number"
    liste = []
    l = len(matrix[0])
    if type(matrix) is not list:
        raise TypeError(messageError)
    for i in matrix:
        if type(i) is not list:
            raise TypeError(messageError)
        if l != len(i):
            raise TypeError(messageErrorB)
    for i in matrix:
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError(messageError)
    if div is None:
        raise ZeroDivisionError("division by zero")
    for m in matrix:
        if not isinstance(div, (int, float)):
            raise TypeError(messageErrorC)
        else:
            for k in m:
                liste.append([round((k / div), 2)])
    return(liste)
