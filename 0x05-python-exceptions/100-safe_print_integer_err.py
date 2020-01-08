#!/usr/bin/python3
def safe_print_integer(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        sys.stderr.write("Eceptionx: {}".format(TypeError))
        return False
