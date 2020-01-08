#!/usr/bin/python3
def safe_print_integer(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        sys.stderr.write("Exception: {}".format(error))
        return False
