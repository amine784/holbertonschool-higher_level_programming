#!/usr/bin/python3
'''ends a request to the URL and displays the value of the X-Request-Id
'''
import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":
        urll_ = argv[1]
        email = {'email': argv[2]}
        data_ = urllib.parse.urlencode(email)
        data = data_.encode('ascii')
        resp = urllib.request.Request(urll_, data)
        with urllib.request.urlopen(resp) as resp:
            print(resp.read().decode("utf-8"))
