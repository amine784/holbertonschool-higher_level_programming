#!/usr/bin/python3
max = 8
for a in range(0, 9):
    for b in range(0, 10):
        if a < b:
            if a < max:
                print("{:d}{:d}, ".format(a, b), end="")
            else:
                print("{:d}{:d}".format(a, b))
