#!/usr/bin/python3
import os
import sys
if __name__ == "__main__":
    l = len(sys.argv)
    s = 0
    for x in range(1, l):
        arg = (sys.argv[x])
        s += int(arg)
print("{:d}".format(s))
