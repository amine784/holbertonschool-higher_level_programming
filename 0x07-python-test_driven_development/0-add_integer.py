def add_integer(a, b=98):
    '''
    function that add 2 integer
    '''
    messageErrorA = "a must be an integer"
    messageErrorB = "b must be an integer"
    x = type(a)
    y = type(b)
    if x is not int and x is not float:
        raise TypeError(messageErrorA)
    if y is not int and y is not float:
        raise TypeError(messageErrorB)
    else:
        return(int(a) + int(b))
