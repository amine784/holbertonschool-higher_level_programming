#!/usr/bin/python3
'''
read file
'''
import json
import sys
import os

liste = []
sv_json = __import__('7-save_to_json_file').save_to_json_file
ld_json = __import__('8-load_from_json_file').load_from_json_file
n = "./add_item.json"
x = "./add_item.json"
if not os.path.exists(n):
    sv_json(liste, x)
liste = ld_json(x)
syst = sys.argv[1:]
for i in syst:
    liste.append(i)
    sv_json(liste, x)
