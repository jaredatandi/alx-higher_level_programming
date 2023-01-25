#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1] # Take the URL as a command line argument

try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(data.decode('utf-8'))
except urllib.error.HTTPError as err:
    print("Error code: ", err.code)

