#!/usr/bin/python3
'''ends a request to the URL and displays the value of the X-Request-Id
'''
import urllib.request
import sys
if __name__ == "__main__":
        try:
            with request.urlopen(sys.argv[1]) as req:
                    print(req.read().decode("utf-8"))
        except error.HTTPError as error:
            print("Error code: {}"format(error.code))
