#!/usr/bin/python3
'''
if __name__ == "__main__":
'''
import os
import sys
l = len(sys.argv)
s = 0
for x in range(1, l):
    arg = (sys.argv[x])
    s += int(arg)
print("{:d}".format(s))
