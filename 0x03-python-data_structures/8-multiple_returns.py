#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        return(0, None)
    elif l > 0:
        return(l, sentence[0])
