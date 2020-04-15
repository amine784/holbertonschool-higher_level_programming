#!/usr/bin/python3
'''script tosends a POST request to the passed URL with the email
'''
from sys import argv
import requests
if __name__ == "__main__":
    if (len(argv) == 1):
        q = ""
    else:
        q = argv[1]
    jason = (requests.post("http://0.0.0.0:5000/search_user")).json()
    if len(jason) == 0:
        print("{}".format("No result"))
    if (jason):
        print("[{}] {}".format(jason.get("id"), jason.get("name")))
    else:
        print("{}".format("Not a valid JASON"))
