#!/usr/bin/python3
'''script tosends a POST request to the passed URL with the email'''
from sys import argv
import requests
if __name__ == "__main__":
    com = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])).json()[:10]
    for i in com:
        a = (i.get('commit').get('author').get('name'))
        print("{}: {}".format(i.get('sha'), a))
