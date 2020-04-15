#!/usr/bin/python3
'''script tosends a POST request to the passed URL with the email
'''
from sys import argv
import requests
if __name__ == "__main__":
    if ((requests.get(argv[1]).status_code >= 400)):
        print("Error code: {}".format(requests.get(argv[1]).status_code))
    else:
        print((requests.get(argv[1])).text)
