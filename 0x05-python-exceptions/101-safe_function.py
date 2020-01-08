#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    res = 0
    try:
        res = fct(*args)
        return(res)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
