#!/usr/bin/python3
'''ends a request to the URL and displays the value of the X-Request-Id
'''
import urllib.request as intranet
import sys
if __name__ == "__main__":
        with intranet.urlopen(sys.argv[1]) as head:
            header = head.getheader("X-Request-Id")
            print(header)
