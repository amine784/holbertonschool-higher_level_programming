#!/usr/bin/python3
'''script to display info from intranet
'''
import urllib.request as intranet
if __name__ == "__main__":
        with intranet.urlopen('https://intranet.hbtn.io/status') as fetch:
                page = fetch.read()
                print("Body response:")
                print("\t- type: {}".format(type(page)))
                print("\t- content: {}".format(page))
                print("\t- utf8 content: {}".format(str(page, "utf-8")))
