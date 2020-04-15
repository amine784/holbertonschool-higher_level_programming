#!/usr/bin/python3
'''script tosends a POST request to the passed URL with the email'''
from sys import argv
import requests
if __name__ == "__main__":
    q = ''
    if (len(argv) == 2):
        q = argv[1]
    try:
        s = (requests.post("http://0.0.0.0:5000/search_user", {"q": q})).json()
        if not s:
            print("{}".format("No result"))
        else:
            print("[{}] {}".format(s.get("id"), s.get("name")))
    except:
        print("{}".format("Not a valid JSON"))
