#!/usr/bin/python3
'''script tosends a POST request to the passed URL with the email'''
from sys import argv
import requests
if __name__ == "__main__":
    js = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(js.json().get('id'))
