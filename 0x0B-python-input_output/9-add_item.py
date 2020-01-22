#!/usr/bin/python3
'''
read file
'''
import json
import sys
import os

sv_json = __import__('7-save_to_json_file').save_to_json_file
ld_json = __import__('8-load_from_json_file').load_from_json_file
liste = []
if not os.path.exists("./add_item.json"):
    sv_json(liste, "add_item.json")
else:
    continue
liste = ld_json("add_item.json")
for i in sys.argv[0:-1]:
    liste.append(i)
    sv_json(liste, "add_item.json")
