#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a + ('0', '0')
    y = tuple_b + ('0', '0')
    a = int(x[0])
    b = int(y[0])
    s = a + b
    c = int(x[1])
    d = int(y[1])
    s1 = c + d
    k = s, s1
    return(k)
