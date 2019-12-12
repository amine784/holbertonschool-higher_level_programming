#!/usr/bin/python3
import os
import sys
l = len(sys.argv)
if l == 1:
    print("{:d} argument.".format(l-1))
if l == 2:
    print("{:d} argument:".format(l-1))
elif l > 2:
    print("{:d} arguments:".format(l-1))
l = len(sys.argv)
for x in range(1, l):
    print("{:d}: {:s}".format(x, (sys.argv[x])))
