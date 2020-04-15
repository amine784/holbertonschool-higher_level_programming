#!/usr/bin/python3
'''script tosends a POST request to the passed URL with the email
'''
from sys import argv
import requests
if __name__ == "__main__":
    print("{}".format((requests.post(argv[1], email={'email': argv[2]}).text)))
