#!/usr/bin/python3
def safe_print_integer(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        sys.stderr.write("Eceptionx: {}".format(ValueError))
        return False
