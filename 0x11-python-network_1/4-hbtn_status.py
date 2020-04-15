#!/usr/bin/python3
'''ends a request to the URL and displays the value of the X-Request-Id
'''
import requests
if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req))
