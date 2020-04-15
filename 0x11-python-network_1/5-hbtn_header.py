#!/usr/bin/python3
'''ends a request to the URL and displays the value of the X-Request-Id
'''
from sys import argv
import requests
if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
